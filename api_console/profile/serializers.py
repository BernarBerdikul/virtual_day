from rest_framework import serializers
from virtual_day.authentication import get_token
from virtual_day.users.models import User
from virtual_day.utils.exceptions import PreconditionFailedException
from datetime import datetime
from virtual_day.utils import constants, messages, codes
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils.validators import password_comparison, validate_image
from virtual_day.utils.decorators import query_debugger


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer in admin console """

    class Meta:
        model = User
        fields = ('id', 'email', 'role', 'avatar', 'phone', 'address',
                  'first_name', 'last_name', 'language')

    def to_representation(self, instance):
        representation = super(
            UserSerializer, self).to_representation(instance)
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
        fields = ('avatar', 'phone', 'address',
                  'first_name', 'last_name', 'language')

    def to_representation(self, instance):
        representation = super(
            UpdateProfileSerializer, self).to_representation(instance)
        representation['avatar'] = get_full_url(instance.avatar)
        return representation


class ChangePasswordSerializer(serializers.Serializer):
    """ change password for user in admin console """
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def change(self):
        user = self.context['user']
        user.set_password(password_comparison(self.validated_data))
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
