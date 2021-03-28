from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from virtual_day.core.models import Schedule
from virtual_day.users.permissions import (
    IsStudent, IsModerator, AnyPermissions
)
from virtual_day.utils import constants
from .serializers import (
    ScheduleListSerializer, ScheduleDetailSerializer
)
from virtual_day.utils.decorators import query_debugger, response_wrapper


@method_decorator(response_wrapper(), name='dispatch')
class ScheduleViewSet(viewsets.ViewSet):
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsStudent, IsModerator]

    @query_debugger
    def list(self, request):
        language = request.query_params.get(
            'language', constants.SYSTEM_LANGUAGE)
        schedules = Schedule.objects.all().translate(language)
        return Response(ScheduleListSerializer(schedules, many=True).data)

    @query_debugger
    def retrieve(self, request, pk=None):
        language = request.query_params.get(
            'language', constants.SYSTEM_LANGUAGE)
        schedules = Schedule.objects.filter(id=pk).translate(language)
        schedule = get_object_or_404(schedules, pk=pk)
        return Response(ScheduleDetailSerializer(schedule).data)
