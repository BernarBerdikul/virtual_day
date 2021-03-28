from rest_framework import serializers
from virtual_day.authentication import get_token
from virtual_day.users.models import User
from virtual_day.utils.exceptions import (
    CommonException, PreconditionFailedException
)
from datetime import datetime
from virtual_day.utils import constants, messages, codes
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils.validators import password_comparison
from virtual_day.utils.decorators import query_debugger


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
        password = password_comparison(validated_data)
        # password = BaseUserManager.make_random_password(self)
        user = User.objects.create(email=email, role=constants.ADMIN)
        user.set_password(password)
        user.save()
        # """ send mail for admin with generated password """
        # asyncio.new_event_loop().run_until_complete(
        #     send_email("Admin", user.email, password))
        return user


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer in admin console """

    class Meta:
        model = User
        fields = ('id', 'email', 'role', 'avatar', 'phone', 'address',
                  'first_name', 'last_name')

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
