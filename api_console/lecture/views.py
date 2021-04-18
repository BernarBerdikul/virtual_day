from django.utils.decorators import method_decorator
from rest_framework import viewsets
from virtual_day.users.permissions import (
    IsAdmin, IsSuperAdmin, AnyPermissions
)
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from virtual_day.core.models import Lecture, Event
from virtual_day.utils.decorators import (
    query_debugger, response_wrapper, except_data_error
)
from .serializers import (
    LectureListSerializer, LectureDetailSerializer, SpeakerSerializer,
    EventSerializer
)
from virtual_day.users.models import User
from virtual_day.utils import constants


@method_decorator(response_wrapper(), name='dispatch')
class LectureViewSet(viewsets.ViewSet):
    """ ViewSet to work with User """
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsSuperAdmin, IsAdmin]

    @query_debugger
    def list(self, request):
        """ get lectures """
        lectures = Lecture.objects.select_related(
            'speaker', 'event'
        ).translate_related(
            'event'
        ).translate(request.user.language).all()
        """ get speakers """
        speakers = User.objects.filter(
            role=constants.SPEAKER, is_active=True,
            first_name__isnull=False, last_name__isnull=False)
        """ get events """
        events = Event.objects.filter(
            event_type=constants.TYPE_LECTURE, enable=True
        ).translate(request.user.language)
        return Response(
            {"model": LectureListSerializer(lectures, many=True).data,
             "speakers": SpeakerSerializer(speakers, many=True).data,
             "events": EventSerializer(events, many=True).data})

    @query_debugger
    def retrieve(self, request, pk=None):
        dod_days = Lecture.objects.filter(pk=pk)
        dod_day = get_object_or_404(dod_days, pk=pk)
        return Response(LectureDetailSerializer(dod_day).data)

    @query_debugger
    @except_data_error
    def create(self, request):
        serializer = LectureDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lecture = serializer.save()
        return Response(LectureListSerializer(lecture).data)

    @query_debugger
    @except_data_error
    def update(self, request, pk=None):
        lectures = Lecture.objects.all()
        instance = get_object_or_404(lectures, pk=pk)
        serializer = LectureDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        lecture = serializer.save()
        return Response(LectureListSerializer(lecture).data)

    @query_debugger
    def destroy(self, request, pk=None):
        dod_days = Lecture.objects.all()
        get_object_or_404(dod_days, pk=pk).delete()
        return Response()
