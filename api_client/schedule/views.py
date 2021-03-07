from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from virtual_day.core.models import Schedule
from virtual_day.users.permissions import IsAdmin
from .serializers import (ScheduleListSerializer, ScheduleDetailSerializer,)
from virtual_day.utils.decorators import query_debugger, response_wrapper
from business_rules.billboard_rules import billboard_rules_response


@method_decorator(response_wrapper(), name='dispatch')
class ScheduleViewSet(viewsets.ViewSet):
    permission_classes = (IsAdmin,)

    @query_debugger
    def list(self, request):
        billboards = Schedule.objects.filter(enable=True).translat(request.user.langauge)
        return Response({"model": ScheduleListSerializer(billboards, many=True).data,
                         "rules": billboard_rules_response})

    @query_debugger
    def retrieve(self, request, pk=None):
        billboards = Schedule.objects.filter(id=pk, enable=True).translat(request.user.langauge)
        billboard = get_object_or_404(billboards, pk=pk)
        return Response(ScheduleDetailSerializer(billboard).data)
