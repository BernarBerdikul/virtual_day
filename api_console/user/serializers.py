from rest_framework import serializers
from virtual_day.authentication import get_token
from virtual_day.users.models import User
from virtual_day.utils.exceptions import (
    CommonException, PreconditionFailedException
)
from datetime import datetime
from virtual_day.utils import constants, messages, codes
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils.validators import validate_password
from django.contrib.auth.base_user import BaseUserManager
from business_service.send_email_service import (
    send_email
)
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
        """ generate password """
        password = BaseUserManager.make_random_password(self)
        user = User.objects.create(email=email, role=constants.ADMIN)
        user.set_password(password)
        user.save()
        """ send mail for admin with generated password """
        send_email("Admin", user.email, password)
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
        representation['avatar'] = get_full_url(instance.avatar)
        return representation


class ChangePasswordSerializer(serializers.Serializer):
    """ change password for user in admin console """
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate(self, attrs):
        """ check if passwords are equal """
        password = validate_password(attrs['password'])
        password_confirm = validate_password(attrs['password'])
        if password != password_confirm:
            raise CommonException(code=codes.VALIDATION_ERROR,
                                  detail=messages.PASSWORD_NOT_EQUAL)
        return attrs

    def change(self):
        user = self.context['user']
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """ Login for user in admin console """
    email = serializers.CharField()
    password = serializers.CharField()

    @query_debugger
    def user_login(self):
        """ authentication and authorisation """
        try:
            user = User.objects.get(email=self.validated_data['email'])
            if not user.check_password(self.validated_data['password']):
                raise PreconditionFailedException(
                    detail={"password": messages.WRONG_EMAIL_OR_PASSWORD},
                    code=codes.AUTH_ERROR)
        except User.DoesNotExist:
            raise PreconditionFailedException(
                detail={"password": messages.WRONG_EMAIL_OR_PASSWORD},
                code=codes.AUTH_ERROR)
        token = get_token(user)
        user.last_login = datetime.now()
        user.save()
        return token, user.role
