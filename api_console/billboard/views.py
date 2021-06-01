from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from business_service.generators import (
    generate_list_type_billboard, generate_list_unique_keys
)
from business_service.service_methods import (
    create_translation, update_translation, json_multipart_checker
)
from virtual_day.core.models import Billboard, Event
from virtual_day.users.permissions import (
    IsAdmin, IsSuperAdmin, AnyPermissions
)
from .serializers import (
    BillboardListSerializer, BillboardDetailSerializer,
    EventSelectSerializer, BillboardCreateSerializer,
    BillboardCreateVideoSerializer, BillboardCreateTextSerializer
)
from virtual_day.utils.decorators import (
    query_debugger, except_data_error, response_wrapper
)
from business_rules.billboard_rules import billboard_rules_response


@method_decorator(response_wrapper(), name='dispatch')
class BillboardViewSet(viewsets.ViewSet):
    """ ViewSet provide CRUD methods to work with Billboard model """
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsSuperAdmin, IsAdmin]
    parser_classes = (MultiPartParser, JSONParser)

    @query_debugger
    def list(self, request):
        """ return all billboards """
        offset = int(request.query_params.get('offset', 0))
        limit = int(request.query_params.get('limit', 10))
        """ get billboards """
        billboards = Billboard.objects.translate(
            request.user.language)[offset: offset + limit]
        """ get events for select """
        events = Event.objects.filter(enable=True).translate(
            request.user.language)
        return Response(
            {"model": BillboardListSerializer(billboards, many=True).data,
             "rules": billboard_rules_response,
             "type_billboard": generate_list_type_billboard(),
             "events": EventSelectSerializer(events, many=True).data,
             "unique_keys": generate_list_unique_keys()})

    @query_debugger
    def retrieve(self, request, pk=None):
        """ return billboard by id with translations """
        billboards = Billboard.objects.filter(
            id=pk).translate(request.user.language)
        billboard = get_object_or_404(billboards, pk=pk)
        """ get events for select """
        events = Event.objects.filter(enable=True).translate(
            request.user.language)
        return Response(
            {"model": BillboardDetailSerializer(billboard).data,
             "rules": billboard_rules_response,
             "type_billboard": generate_list_type_billboard(),
             "events": EventSelectSerializer(events, many=True).data,
             "unique_keys": generate_list_unique_keys()})

    @query_debugger
    @except_data_error
    def create(self, request):
        """ create billboard with translations """
        serializer = BillboardCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        billboard = serializer.save()
        """ create translations """
        create_translation(
            translations=json_multipart_checker(request.data['translations']),
            object_id=billboard.id, model=Billboard)
        result_billboard = Billboard.objects.translate(
            request.user.language).get(id=billboard.id)
        return Response(BillboardListSerializer(result_billboard).data)

    @query_debugger
    @except_data_error
    def partial_update(self, request, pk=None):
        """ update billboard with translations """
        billboards = Billboard.objects.filter(id=pk, enable=True)
        instance = get_object_or_404(billboards, pk=pk)
        serializer = BillboardDetailSerializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        billboard = serializer.save()
        """ create translations """
        update_translation(
            translations=json_multipart_checker(request.data['translations']),
            model=Billboard, object_id=pk)
        result_billboard = Billboard.objects.translate(
            request.user.language).get(id=billboard.id)
        return Response(BillboardListSerializer(result_billboard).data)

    @query_debugger
    def destroy(self, request, pk=None):
        """ delete object by id """
        billboard = Billboard.objects.filter(id=pk)
        get_object_or_404(billboard, pk=pk).delete()
        return Response()
