from rest_framework import serializers
from virtual_day.users.models import User
from virtual_day.utils import constants
from virtual_day.utils.image_utils import get_full_url
from virtual_day.core.models import Lecture, Event


class SpeakerEventSerializer(serializers.ModelSerializer):
    """ Schedule serializer for detail information """

    class Meta:
        model = Event
        fields = ('id', 'period_start', 'period_end', 'title', 'event_type')


class SpeakerLectureSerializer(serializers.ModelSerializer):
    """  """
    class Meta:
        model = Lecture
        fields = ('id', 'class_room', 'event')

    def to_representation(self, instance):
        representation = super(
            SpeakerLectureSerializer, self).to_representation(instance)
        representation['event'] = SpeakerEventSerializer(instance.event).data
        return representation


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
        representation['avatar'] = get_full_url(instance.avatar)
        return representation


class ChangeUserActiveSerializer(serializers.ModelSerializer):
    """ Serializer for change user is_active field in admin console """

    class Meta:
        model = User
        fields = ('is_active',)
