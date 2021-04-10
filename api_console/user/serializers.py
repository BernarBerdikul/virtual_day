from django.contrib.auth.base_user import BaseUserManager
from rest_framework import serializers
from business_service.send_email_service import send_email
from virtual_day.users.models import User
from virtual_day.utils import constants
from virtual_day.utils.decorators import query_debugger
from asgiref.sync import sync_to_async


class CreateAdminSerializer(serializers.ModelSerializer):
    """ Serializer for registration """
    class Meta:
        model = User
        fields = ('email',)

    @query_debugger
    def create_admin(self, validated_data):
        """ Register new user """
        email = validated_data.get("email")
        """ comparison of password """
        password = BaseUserManager.make_random_password(self)
        user = User.objects.create(email=email, role=constants.ADMIN)
        user.set_password(password)
        user.save()
        """ send mail for admin with generated password """
        sync_to_async(send_email("Admin", user.email, password))
        return user


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer in admin console """

    class Meta:
        model = User
        fields = ('id', 'email', 'role', 'avatar', 'phone', 'address',
                  'first_name', 'last_name', 'is_active')

    def to_representation(self, instance):
        representation = super(
            UserSerializer, self).to_representation(instance)
        representation['role'] = constants.USER_TYPES[instance.role][1]
        return representation


class ChangeUserRoleSerializer(serializers.ModelSerializer):
    """ Serializer for change user role in admin console """

    class Meta:
        model = User
        fields = ('role',)


class ChangeUserActiveSerializer(serializers.ModelSerializer):
    """ Serializer for change user is_active field in admin console """

    class Meta:
        model = User
        fields = ('is_active',)
