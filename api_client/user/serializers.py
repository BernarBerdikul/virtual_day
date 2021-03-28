from rest_framework import serializers
from virtual_day.authentication import get_token
from virtual_day.users.models import User
from virtual_day.utils.exceptions import (
    CommonException, PreconditionFailedException
)
from datetime import datetime
from virtual_day.utils import constants, messages, codes
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils.validators import (
    validate_password, validate_image
)
from django.contrib.auth.base_user import BaseUserManager
from business_service.send_email_service import send_email
from virtual_day.utils.decorators import query_debugger


class RegisterSerializer(serializers.ModelSerializer):
    """ Serializer for registration """
    class Meta:
        model = User
        fields = ('email', 'phone', 'address', 'first_name', 'last_name')

    def register(self, validated_data):
        """ Register new user """
        """ generate password """
        password = BaseUserManager.make_random_password(self)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        """ send mail for user with generated password """
        send_email(user.first_name, user.email, password)
        return user


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer in client application """

    class Meta:
        model = User
        fields = ('email', 'role', 'avatar', 'phone', 'address',
                  'first_name', 'last_name')

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        representation['role'] = constants.USER_TYPES[instance.role][1]
        representation['avatar'] = get_full_url(instance.avatar)
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    """ Serializer for update user's profile in client application """
    avatar = serializers.ImageField(
        max_length=None, use_url=True,
        required=False, validators=[validate_image])

    class Meta:
        model = User
        fields = ('avatar', 'phone', 'address', 'first_name', 'last_name')


class ChangePasswordSerializer(serializers.Serializer):
    """ change password for user in client application """
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate(self, attrs):
        """ check if passwords are equal """
        password = validate_password(attrs['password'])
        password_confirm = validate_password(attrs['password'])
        if password != password_confirm:
            raise CommonException(code=codes.VALIDATION_ERROR, detail=messages.PASSWORD_NOT_EQUAL)
        return attrs

    def change(self):
        user = self.context['user']
        user.set_password(self.validated_data['password'])
        user.save()
        return user


# class EnterEmailSerializer(serializers.Serializer):
#     """ change email for user in client application """
#     email = serializers.EmailField()
#
#     def validate(self, attrs):
#         """ validate the email if email already exist in database """
#         if User.objects.filter(email=attrs['email']).exclude(
#                 id=self.context['user'].id).count() > 0:
#             raise CommonException(code=codes.ALREADY_EXISTS,
#                                   detail=messages.EMAIL_ALREADY_EXISTS)
#         return attrs
#
#     def update_email(self):
#         """ method get User and update his email """
#         user = User.objects.get(id=self.context['user'].id)
#         user.email = self.validated_data['email']
#         user.save()
#         return manager


class LoginSerializer(serializers.Serializer):
    """ Login for user in client application """
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
