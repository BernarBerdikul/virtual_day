from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from virtual_day.core.models import Schedule
from virtual_day.users.permissions import IsStudent, IsModerator, AnyPermissions
from .serializers import (ScheduleListSerializer, ScheduleDetailSerializer,)
from virtual_day.utils.decorators import query_debugger, response_wrapper


@method_decorator(response_wrapper(), name='dispatch')
class ScheduleViewSet(viewsets.ViewSet):
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsStudent, IsModerator]

    @query_debugger
    def list(self, request):
        schedules = Schedule.objects.all().translate(request.user.language)
        return Response(ScheduleListSerializer(schedules, many=True).data)

    @query_debugger
    def retrieve(self, request, pk=None):
        schedules = Schedule.objects.filter(id=pk).translate(request.user.language)
        schedule = get_object_or_404(schedules, pk=pk)
        return Response(ScheduleDetailSerializer(schedule).data)
