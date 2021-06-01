from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from business_rules.schedule_rules import schedule_rules_response
from business_service.service_methods import (
    create_translation, update_translation, json_multipart_checker
)
from virtual_day.core.models import Event, DodDay
from virtual_day.users.permissions import (
    IsAdmin, IsSuperAdmin, AnyPermissions
)
from .serializers import (
    EventListSerializer, EventDetailSerializer
)
from virtual_day.utils.decorators import (
    query_debugger, except_data_error, response_wrapper
)
from virtual_day.utils import constants
from ..dod_day.serializers import DodDaySerializer
from django.db import transaction


@method_decorator(response_wrapper(), name='dispatch')
class EventViewSet(viewsets.ViewSet):
    """ ViewSet provide CRUD methods to work with Schedule model """
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsSuperAdmin, IsAdmin]

    @query_debugger
    def list(self, request):
        """ return all events """
        offset = int(request.query_params.get('offset', 0))
        limit = int(request.query_params.get('limit', 10))
        events = Event.objects.select_related('dod_day').translate(
            request.user.language)[offset: offset + limit]
        dod_days = DodDay.objects.all()
        event_types = [{"value": value, "label": label}
                       for value, label in constants.EVENT_TYPE]
        return Response(
            {"model": EventListSerializer(events, many=True).data,
             "dod_day": DodDaySerializer(dod_days, many=True).data,
             "event_types": event_types,
             "rules": schedule_rules_response})

    @query_debugger
    def retrieve(self, request, pk=None):
        """ return event by id with translations """
        events = Event.objects.filter(id=pk).translate(request.user.language)
        event = get_object_or_404(events, pk=pk)
        return Response(EventDetailSerializer(event).data)

    @query_debugger
    @except_data_error
    @transaction.atomic()
    def create(self, request):
        """ create event with translations """
        serializer = EventDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = serializer.save()
        """ create translations """
        create_translation(
            translations=json_multipart_checker(request.data['translations']),
            model=Event, object_id=event.id)
        result_schedule = Event.objects.translate(
            request.user.language).get(id=event.id)
        return Response(EventListSerializer(result_schedule).data)

    @query_debugger
    @except_data_error
    @transaction.atomic()
    def partial_update(self, request, pk=None):
        """ update event with translations """
        events = Event.objects.filter(id=pk)
        instance = get_object_or_404(events, pk=pk)
        serializer = EventDetailSerializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        """ update translations """
        update_translation(
            translations=json_multipart_checker(request.data['translations']),
            model=Event, object_id=pk)
        event = Event.objects.translate(request.user.language).get(id=pk)
        return Response(EventListSerializer(event).data)

    @query_debugger
    def destroy(self, request, pk=None):
        schedule = Event.objects.filter(id=pk)
        get_object_or_404(schedule, pk=pk).delete()
        return Response()
