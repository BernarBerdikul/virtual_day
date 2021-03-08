from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from business_rules.schedule_rules import schedule_rules_response
from business_service.service_methods import create_translation, update_translation
from virtual_day.core.models import Schedule, Billboard
from virtual_day.users.permissions import IsAdmin
from .serializers import (ScheduleListSerializer, BillboardShortListSerializer, ScheduleDetailSerializer,)
from virtual_day.utils.decorators import query_debugger, except_data_error, response_wrapper


@method_decorator(response_wrapper(), name='dispatch')
class ScheduleViewSet(viewsets.ViewSet):
    """ ViewSet provide CRUD methods to work with Schedule model """
    permission_classes = (IsAdmin,)

    @query_debugger
    def list(self, request):
        """ return all schedules """
        schedules = Schedule.objects.all().translate(request.user.language)
        billboards = Billboard.objects.filter(enable=True).translate(request.user.language)
        return Response({"model": ScheduleListSerializer(schedules, many=True).data,
                         "billboards": BillboardShortListSerializer(billboards, many=True).data,
                         "rules": schedule_rules_response})

    @query_debugger
    def retrieve(self, request, pk=None):
        """ return schedule by id with translations """
        schedules = Schedule.objects.filter(id=pk).translate(request.user.language)
        schedule = get_object_or_404(schedules, pk=pk)
        return Response(ScheduleDetailSerializer(schedule).data)

    @query_debugger
    @except_data_error
    def create(self, request):
        """ create schedule with translations """
        serializer = ScheduleDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedule = serializer.save()
        """ create translations """
        create_translation(model=Schedule, translations=request.data['translations'], object_id=schedule.id)
        result_schedule = Schedule.objects.translate(request.user.language).get(id=schedule.id)
        return Response(ScheduleListSerializer(result_schedule).data)

    @query_debugger
    @except_data_error
    def partial_update(self, request, pk=None):
        """ update schedule with translations """
        schedules = Billboard.objects.filter(id=pk)
        instance = get_object_or_404(schedules, pk=pk)
        serializer = ScheduleDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        """ update translations """
        update_translation(model=Schedule, translations=request.data['translations'], object_id=pk)
        result_schedule = Schedule.objects.translate(request.user.language).get(id=pk)
        return Response(ScheduleListSerializer(result_schedule).data)

    @query_debugger
    def destroy(self, request, pk=None):
        schedule = Schedule.objects.filter(id=pk)
        get_object_or_404(schedule, pk=pk).delete()
        return Response()
