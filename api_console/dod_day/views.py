from django.utils.decorators import method_decorator
from rest_framework import viewsets
from virtual_day.users.permissions import (
    IsAdmin, IsSuperAdmin, AnyPermissions
)
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from virtual_day.core.models import DodDay
from virtual_day.utils.decorators import (
    query_debugger, response_wrapper, except_data_error
)
from .serializers import DodDaySerializer


@method_decorator(response_wrapper(), name='dispatch')
class DodDayViewSet(viewsets.ViewSet):
    """ ViewSet to work with User """
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsSuperAdmin, IsAdmin]

    @query_debugger
    def list(self, request):
        offset = int(request.query_params.get('offset', 0))
        limit = int(request.query_params.get('limit', 10))
        dod_days = DodDay.objects.all()[offset: offset + limit]
        return Response(DodDaySerializer(dod_days, many=True).data)

    @query_debugger
    def retrieve(self, request, pk=None):
        dod_days = DodDay.objects.filter(pk=pk)
        dod_day = get_object_or_404(dod_days, pk=pk)
        return Response(DodDaySerializer(dod_day).data)

    @query_debugger
    @except_data_error
    def create(self, request):
        serializer = DodDaySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @query_debugger
    @except_data_error
    def update(self, request, pk=None):
        dod_days = DodDay.objects.filter(pk=pk)
        dod_day = get_object_or_404(dod_days, pk=pk)
        serializer = DodDaySerializer(dod_day, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @query_debugger
    def destroy(self, request, pk=None):
        dod_days = DodDay.objects.filter(pk=pk)
        get_object_or_404(dod_days, pk=pk).delete()
        return Response()
