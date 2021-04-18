from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from business_service.generators import generate_list_roles
from virtual_day.users.models import User
from virtual_day.users.permissions import IsSuperAdmin
from virtual_day.utils.decorators import query_debugger, response_wrapper
from .serializers import (
    CreateAdminSerializer, UserSerializer,
    ChangeUserRoleSerializer, ChangeUserActiveSerializer
)
from rest_framework.generics import get_object_or_404
from virtual_day.utils import constants
from .service import export_excel_file


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
    @action(methods=['POST'], detail=False)
    def search(self, request):
        """ search users by email """
        users = User.objects.filter(email__icontains=request.data['title'])
        return Response(UserSerializer(users, many=True).data)

    @query_debugger
    def list(self, request):
        """ return all users or by role """
        users = User.objects.all()
        role = request.query_params.get('role', None)
        if role:
            users = User.objects.filter(role=role)
        return Response(
            {"model": UserSerializer(users, many=True).data,
             "roles": generate_list_roles()})

    @query_debugger
    def update(self, request, pk=None):
        """ method for change user role """
        users = User.objects.exclude(role=constants.SUPER_ADMIN)
        user = get_object_or_404(users, pk=pk)
        serializer = ChangeUserRoleSerializer(
            user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_user = serializer.save()
        return Response(UserSerializer(updated_user).data)

    @query_debugger
    def partial_update(self, request, pk=None):
        """ change user's is_active status """
        users = User.objects.exclude(role=constants.SUPER_ADMIN)
        instance = get_object_or_404(users, pk=pk)
        serializer = ChangeUserActiveSerializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data)

    @query_debugger
    @action(methods=['GET'], detail=False)
    def export_users_excel(self, request):
        """ method for change user role """
        result_link = export_excel_file()
        return Response({"download_link": result_link})
