from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from virtual_day.core.models import Billboard
from virtual_day.users.permissions import (
    IsStudent, IsModerator, AnyPermissions
)
from .serializers import (
    BillboardListSerializer, BillboardDetailSerializer
)
from virtual_day.utils.decorators import query_debugger, response_wrapper
from virtual_day.utils import constants


@method_decorator(response_wrapper(), name='dispatch')
class BillboardViewSet(viewsets.ViewSet):
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsStudent, IsModerator]

    @query_debugger
    def list(self, request):
        language = request.query_params.get(
            'language', constants.SYSTEM_LANGUAGE)
        billboards = Billboard.objects.filter(enable=True).translate(language)
        static_billboards = billboards.filter(is_static=True)
        dynamic_billboards = billboards.filter(is_static=False)
        return Response(
            {"static_billboards": BillboardListSerializer(
                static_billboards, many=True).data,
             "dynamic_billboards": BillboardListSerializer(
                 dynamic_billboards, many=True).data})

    @query_debugger
    def retrieve(self, request, pk=None):
        language = request.query_params.get(
            'language', constants.SYSTEM_LANGUAGE)
        billboards = Billboard.objects.filter(
            id=pk, enable=True).translate(language)
        billboard = get_object_or_404(billboards, pk=pk)
        return Response(BillboardDetailSerializer(billboard).data)
