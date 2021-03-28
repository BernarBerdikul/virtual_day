from django.utils.decorators import method_decorator
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from virtual_day.users.models import User
from virtual_day.users.permissions import (
    IsAdmin, IsSuperAdmin, AnyPermissions
)
from virtual_day.utils.decorators import query_debugger, response_wrapper
from .serializers import (
    RegisterSerializer, UserSerializer, LoginSerializer,
    ChangePasswordSerializer
)
from virtual_day.utils import constants


@method_decorator(response_wrapper(), name='dispatch')
class UserViewSet(viewsets.ViewSet):
    """ ViewSet to work with User """
    permission_classes = (AnyPermissions,)
    any_permission_classes = [IsSuperAdmin, IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @query_debugger
    @action(methods=['POST'], permission_classes=(IsSuperAdmin,), detail=False)
    def create_admin(self, request):
        """ method for create admin for admin console """
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        manager = serializer.register(request.data)
        return Response(UserSerializer(manager).data)

    @query_debugger
    @action(methods=['GET'], detail=False)
    def get_profile(self, request):
        """ method return user profile """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

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
        serializer = UserSerializer(
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
