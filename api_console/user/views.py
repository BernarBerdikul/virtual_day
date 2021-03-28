from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from virtual_day.users.models import User
from virtual_day.users.permissions import IsSuperAdmin
from virtual_day.utils.decorators import query_debugger, response_wrapper
from .serializers import (
    CreateAdminSerializer, UserSerializer, ChangeUserRoleSerializer
)
from virtual_day.utils import constants
from rest_framework.generics import get_object_or_404


@method_decorator(response_wrapper(), name='dispatch')
class UserViewSet(viewsets.ViewSet):
    """ ViewSet to work with User """
    permission_classes = (IsSuperAdmin,)
    serializer_class = UserSerializer

    @query_debugger
    @action(methods=['POST'], detail=False)
    def create_admin(self, request):
        """ method for create admin for admin console """
        serializer = CreateAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create_admin(request.data)
        return Response(UserSerializer(user).data)

    @query_debugger
    def list(self, request):
        """ return users by role """
        users = User.objects.all()
        role = request.query_params.get('role', None)
        if role:
            users = User.objects.filter(role=role)
        return Response(UserSerializer(users, many=True).data)

    @query_debugger
    @action(methods=['POST'], detail=False)
    def change_role(self, request):
        """ method for change user role """
        users = User.objects.all()
        user = get_object_or_404(users, pk=request.data['user_id'])
        serializer = ChangeUserRoleSerializer(
            user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_user = serializer.save()
        return Response(UserSerializer(updated_user).data)
