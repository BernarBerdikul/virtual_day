from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from virtual_day.core.models import Event, Billboard, DodDay
from virtual_day.users.models import User
from virtual_day.users.permissions import (
    IsStudent, IsModerator, AnyPermissions, IsSpeaker
)
from virtual_day.utils import constants
from .serializers import (
    EventListSerializer, EventDetailSerializer,
    SpeakersSerializer, BillboardShortListSerializer
)
from virtual_day.utils.decorators import query_debugger, response_wrapper
from datetime import datetime


@method_decorator(response_wrapper(), name='dispatch')
class EventViewSet(viewsets.ViewSet):
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsStudent, IsModerator, IsSpeaker]

    @query_debugger
    def list(self, request):
        """ return list of events in dod day """
        today_date = datetime.date(datetime.now())
        """ check if today dod day """
        dod_days = DodDay.objects.filter(
            day_date=today_date, enable=True)
        dod_day = get_object_or_404(dod_days, day_date=today_date)
        language = request.headers.get('Accept-Language')
        events = Event.objects.filter(dod_day=dod_day).translate(language)
        return Response(EventListSerializer(events, many=True).data)

    @query_debugger
    def retrieve(self, request, pk=None):
        """ return list of events in dod day """
        today_date = datetime.date(datetime.now())
        """ check if today dod day """
        dod_days = DodDay.objects.filter(
            day_date=today_date, enable=True)
        dod_day = get_object_or_404(dod_days, day_date=today_date)
        language = request.headers.get('Accept-Language')
        events = Event.objects.filter(
            id=pk, dod_day=dod_day).translate(language)
        event = get_object_or_404(events, pk=pk)
        return Response(EventDetailSerializer(event).data)
