from datetime import datetime, timedelta, time
from rest_framework import serializers
from virtual_day.users.models import UserPushNotification
from virtual_day.utils import messages, codes
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils.validators import validate_image
from virtual_day.utils.exceptions import CommonException
from virtual_day.utils.support_code.timestamp_converter import (
    convert_datetime_with_short_month
)


class PushListSerializer(serializers.ModelSerializer):
    """ list Serializer for pushes """

    class Meta:
        model = UserPushNotification
        fields = ('id', 'image', 'title', 'description', 'date_publication',
                  'users_count', 'views_count', 'is_sent')

    def to_representation(self, instance):
        """ overwrite serializer representation method
        to show image and date_publication """
        representation = super(
            PushListSerializer, self).to_representation(instance)
        representation['image'] = get_full_url(instance.image)
        date_publication = datetime.fromtimestamp(instance.date_publication)
        representation['date_publication'] = \
            convert_datetime_with_short_month(datetime=date_publication)
        return representation


class PushDetailSerializer(serializers.ModelSerializer):
    """ detail Serializer for push """

    class Meta:
        model = UserPushNotification
        fields = ('id', 'title', 'description', 'date_publication',)

    def to_representation(self, instance):
        """ overwrite serializer representation method to show image """
        representation = super(
            PushDetailSerializer, self).to_representation(instance)
        representation['image'] = get_full_url(instance.image)
        return representation


class PushCreateSerializer(PushDetailSerializer):
    """ Serializer for create push"""

    # def validate(self, attrs):
    #     day = datetime.now().date()
    #     tomorrow = day + timedelta(1)
    #     today_start = datetime.combine(day, time())
    #     today_end = datetime.combine(tomorrow, time())
    #     if UserPushNotification.objects.filter(
    #             created_at__lte=today_end,
    #             created_at__gte=today_start).exists():
    #         raise CommonException(
    #             code=codes.VALIDATION_ERROR,
    #             detail=messages.PUSH_LIMIT_MESSAGE)
    #     return attrs


class PushImageSerializer(serializers.ModelSerializer):
    """ PushNotification Serializer to upload
        push's image in admin console """
    image = serializers.ImageField(
        max_length=None, use_url=True,
        required=False, validators=[validate_image])

    class Meta:
        model = UserPushNotification
        fields = ('image',)
