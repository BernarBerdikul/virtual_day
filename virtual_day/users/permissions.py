from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.decorators import permission_classes
from virtual_day.utils import constants
from .models import User


@permission_classes([IsAuthenticated])
class IsStudent(BasePermission):
    """ Permissions for Student """
    def has_permission(self, request, view):
        return User.objects.filter(id=request.user.id, role=constants.STUDENT).exists()


@permission_classes([IsAuthenticated])
class IsAdmin(BasePermission):
    """ Permissions for Admin """
    def has_permission(self, request, view):
        return User.objects.filter(id=request.user.id, role=constants.ADMIN).exists()
