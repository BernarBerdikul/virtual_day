from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from virtual_day.core.models import Event, Billboard
from virtual_day.users.models import User
from virtual_day.users.permissions import (
    IsStudent, IsModerator, AnyPermissions
)
from virtual_day.utils import constants
from .serializers import (
    EventListSerializer, EventDetailSerializer,
    SpeakersSerializer, BillboardShortListSerializer
)
from virtual_day.utils.decorators import query_debugger, response_wrapper


@method_decorator(response_wrapper(), name='dispatch')
class EventViewSet(viewsets.ViewSet):
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsStudent, IsModerator]

    @query_debugger
    def list(self, request):
        language = request.query_params.get(
            'language', constants.SYSTEM_LANGUAGE)
        schedules = Event.objects.translate(language)
        return Response(EventListSerializer(schedules, many=True).data)

    @query_debugger
    def retrieve(self, request, pk=None):
        language = request.query_params.get(
            'language', constants.SYSTEM_LANGUAGE)
        schedules = Event.objects.filter(id=pk).translate(language)
        schedule = get_object_or_404(schedules, pk=pk)
        billboards = Billboard.objects.filter(
            enable=True).translate(request.user.language)
        speakers = User.objects.filter(
            is_active=True, role=constants.SPEAKER)
        return Response(
            {"model": EventDetailSerializer(schedule).data,
             "billboards": BillboardShortListSerializer(billboards, many=True).data,
             "speakers": SpeakersSerializer(speakers, many=True).data})
