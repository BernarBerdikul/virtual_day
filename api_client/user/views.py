from django.db.models import Q
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from virtual_day.users.models import User
from virtual_day.core.models import Lecture
from virtual_day.users.permissions import IsModerator, IsSpeaker
from virtual_day.utils.decorators import query_debugger, response_wrapper
from .serializers import (
    UserSerializer, ChangeUserActiveSerializer, SpeakerLectureSerializer
)
from rest_framework.generics import get_object_or_404
from virtual_day.utils import constants


@method_decorator(response_wrapper(), name='dispatch')
class UserViewSet(viewsets.ViewSet):
    """ ViewSet to work with User """
    permission_classes = (IsModerator,)

    @query_debugger
    def partial_update(self, request, pk=None):
        """ change user's is_active status """
        users = User.objects.filter(
            Q(role=constants.SPEAKER) | Q(role=constants.STUDENT))
        instance = get_object_or_404(users, pk=pk)
        serializer = ChangeUserActiveSerializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data)

    @query_debugger
    @action(methods=['GET'], permission_classes=(IsSpeaker,), detail=False)
    def my_lectures(self, request):
        lectures = Lecture.objects.filter(
            enable=True, speaker_id=request.user.id
        ).translate(request.user.language)
        return Response(SpeakerLectureSerializer(lectures, many=True).data)
