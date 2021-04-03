import datetime
from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from virtual_day.users.permissions import IsSuperAdmin, IsAdmin, AnyPermissions
from virtual_day.users.models import UserPushNotification
from virtual_day.utils.decorators import except_data_error, query_debugger
from .serializers import (
    PushListSerializer, PushImageSerializer,
    PushDetailSerializer, PushCreateSerializer,
)
from business_rules.user_push_notification_rules import (
    user_push_notification_rules_response
)
from .service import check_push_is_not_sent, calculate_pushes_info


class UserPushNotificationViewSet(viewsets.ViewSet):
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsSuperAdmin, IsAdmin]
    parser_classes = (MultiPartParser, JSONParser)

    @query_debugger
    def list(self, request):
        archive = bool(request.query_params.get('archive', False))
        now_in_seconds = datetime.timestamp(datetime.now())
        if archive is True:
            pushes = UserPushNotification.objects.filter(
                date_publication__lte=now_in_seconds)
        else:
            pushes = UserPushNotification.objects.filter(
                date_publication__gte=now_in_seconds, is_sent=False)
        return Response(
            {"model": PushListSerializer(pushes, many=True).data,
             "rules": user_push_notification_rules_response})

    @query_debugger
    def retrieve(self, request, pk=None):
        pushes = UserPushNotification.objects.filter(id=pk)
        push = get_object_or_404(pushes, pk=pk)
        return Response(
            {"model": PushDetailSerializer(push).data,
             "rules": user_push_notification_rules_response})

    @query_debugger
    @except_data_error
    def create(self, request):
        """ push create method """
        serializer = PushCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        push = serializer.save()
        if "image" in request.data and request.data['image'] is not None:
            """ save push's image """
            serializer_image = PushImageSerializer(push, data=request.data)
            serializer_image.is_valid(raise_exception=True)
            serializer_image.save()
        calculated_push = calculate_pushes_info(push_notification=push)
        return Response(PushListSerializer(calculated_push).data,
                        status=status.HTTP_201_CREATED)

    @query_debugger
    @except_data_error
    def partial_update(self, request, pk):
        """ method for update push with translations """
        pushes = UserPushNotification.objects.filter(id=pk)
        instance = get_object_or_404(pushes, pk=pk)
        """ check if push already sent """
        check_push_is_not_sent(push=instance)
        """ update push """
        serializer = PushDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        push = serializer.save()
        if "image" in request.data and request.data['image'] is not None:
            """ save push's image """
            serializer_image = PushImageSerializer(push, data=request.data)
            serializer_image.is_valid(raise_exception=True)
            serializer_image.save()
        calculated_push = calculate_pushes_info(push_notification=push)
        return Response(PushListSerializer(calculated_push).data)

    @query_debugger
    def destroy(self, request, pk=None):
        pushes = UserPushNotification.objects.filter(id=pk)
        get_object_or_404(pushes, pk=pk).delete()
        return Response()
