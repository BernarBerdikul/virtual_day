from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from business_service.generators import generate_list_language
from virtual_day.users.permissions import (
    IsAdmin, IsSuperAdmin, AnyPermissions
)
from virtual_day.utils.decorators import query_debugger, response_wrapper
from .serializers import (
    UserSerializer, LoginSerializer, ChangePasswordSerializer,
    UpdateProfileSerializer
)
from virtual_day.utils import constants


@method_decorator(response_wrapper(), name='dispatch')
class ProfileViewSet(viewsets.ViewSet):
    """ ViewSet to work with User """
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsSuperAdmin, IsAdmin]
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, JSONParser)

    @query_debugger
    @action(methods=['GET'], detail=False)
    def get_profile(self, request):
        """ method return user profile """
        serializer = UserSerializer(request.user)
        return Response({"model": serializer.data,
                         "language_list": generate_list_language()})

    @query_debugger
    @action(methods=['POST'], permission_classes=[AllowAny], detail=False)
    def login(self, request):
        """ user login method """
        serializer = LoginSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        result = serializer.user_login()
        return Response({"token": result[0],
                         "role": constants.USER_TYPES[result[1]][1]})

    @query_debugger
    @action(methods=['POST'], detail=False)
    def update_profile(self, request):
        """ method to update user profile data """
        serializer = UpdateProfileSerializer(
            request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @query_debugger
    @action(methods=['POST'], detail=False)
    def update_password(self, request):
        """ method to update user's password """
        serializer = ChangePasswordSerializer(
            context={'user': request.user}, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.change()
        return Response(UserSerializer(user).data)
