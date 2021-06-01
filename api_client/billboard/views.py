from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from virtual_day.core.models import Billboard, DodDay
from virtual_day.users.permissions import (
    IsStudent, IsModerator, AnyPermissions, IsSpeaker
)
from .serializers import BillboardDetailSerializer
from virtual_day.utils.decorators import query_debugger, response_wrapper
from datetime import datetime


@method_decorator(response_wrapper(), name='dispatch')
class BillboardViewSet(viewsets.ViewSet):
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsStudent, IsModerator, IsSpeaker]

    @query_debugger
    def list(self, request):
        """ return list of stands/billboards """
        today_date = datetime.date(datetime.now())
        """ check if today dod day """
        dod_days = DodDay.objects.filter(
            day_date=today_date, enable=True)
        dod_day = get_object_or_404(dod_days, day_date=today_date)
        """ get billboards """
        language = request.headers.get('Accept-Language')
        billboards = Billboard.objects.filter(
            enable=True, event__dod_day=dod_day
        ).translate(language)
        static_billboards = billboards.filter(is_static=True)
        dynamic_billboards = billboards.filter(is_static=False)
        return Response(
            {"static_billboards": BillboardDetailSerializer(
                static_billboards, many=True,
                context={"language": language}
            ).data,
             "dynamic_billboards": BillboardDetailSerializer(
                 dynamic_billboards, many=True,
                 context={"language": language}
             ).data})

    @query_debugger
    def retrieve(self, request, pk=None):
        """ return detail of specific stand/billboard """
        today_date = datetime.date(datetime.now())
        """ check if today dod day """
        dod_days = DodDay.objects.filter(
            day_date=today_date, enable=True)
        dod_day = get_object_or_404(dod_days, day_date=today_date)
        """ get billboard """
        language = request.headers.get('Accept-Language')
        billboards = Billboard.objects.filter(
            id=pk, enable=True, event__dod_day=dod_day
        ).translate(language)
        billboard = get_object_or_404(billboards, pk=pk)
        return Response(BillboardDetailSerializer(
            billboard, context={"language": language}).data)
