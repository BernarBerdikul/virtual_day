from rest_framework import serializers
from virtual_day.core.models import Event, Billboard, Lecture
from virtual_day.users.models import User
from virtual_day.utils import constants
from virtual_day.utils.image_utils import get_full_url


class SpeakerSerializer(serializers.ModelSerializer):
    """ Serializer for lecture's speaker """
    username = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'avatar')

    def to_representation(self, instance):
        representation = super(
            SpeakerSerializer, self).to_representation(instance)
        representation['avatar'] = get_full_url(instance.avatar)
        return representation

    def get_username(self, obj):
        return f"{obj.last_name} {obj.first_name}"


class LectureSerializer(serializers.ModelSerializer):
    """ Serializer for event's lecture """
    class Meta:
        model = Lecture
        fields = ('class_room', 'speaker',)

    def to_representation(self, instance):
        representation = super(
            LectureSerializer, self).to_representation(instance)
        representation['class_room'] = \
            constants.CLASS_ROOM[instance.class_room][1]
        representation['speaker'] = SpeakerSerializer(instance.speaker).data
        return representation


class EventListSerializer(serializers.ModelSerializer):
    """ Event serializer for short information in list """

    class Meta:
        model = Event
        fields = ('id', 'period_start', 'period_end', 'title', 'event_type')

    def to_representation(self, instance):
        representation = super(
            EventListSerializer, self).to_representation(instance)
        representation['event_type'] = \
            constants.EVENT_TYPE[instance.event_type][1]
        if instance.event_type == constants.TYPE_LECTURE:
            lecture = Lecture.objects.filter(event_id=instance.id)
            if lecture.exists():
                representation['lecture'] = LectureSerializer(lecture).data
        return representation


class EventDetailSerializer(serializers.ModelSerializer):
    """ Schedule serializer for detail information """

    class Meta:
        model = Event
        fields = ('id', 'period_start', 'period_end', 'title', 'event_type')

    def to_representation(self, instance):
        representation = super(
            EventDetailSerializer, self).to_representation(instance)
        return representation


class SpeakersSerializer(serializers.ModelSerializer):
    """ Speakers list serializer for select in mobile app """
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='first_name')

    class Meta:
        model = User
        fields = ('value', 'label',)


class BillboardShortListSerializer(serializers.ModelSerializer):
    """ Billboard serializer for select in mobile app """
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='title')

    class Meta:
        model = Billboard
        fields = ('value', 'label',)
