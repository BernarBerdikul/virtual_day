from rest_framework import serializers
from virtual_day.core.models import Lecture, Event
from virtual_day.users.models import User


class EventSerializer(serializers.ModelSerializer):
    """ Event Serializer for select in admin console """
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='title')

    class Meta:
        model = Event
        fields = ('value', 'label')


class SpeakerSerializer(serializers.ModelSerializer):
    """ Speaker Serializer for select in admin console """
    value = serializers.IntegerField(source='id')
    label = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('value', 'label')

    def get_label(self, obj):
        """ return name of speaker """
        return f"{obj.last_name} {obj.first_name}"


class LectureListSerializer(serializers.ModelSerializer):
    """ Lecture Serializer for list in admin console """

    class Meta:
        model = Lecture
        fields = ('id', 'class_room', 'speaker', 'event', 'enable')

    def to_representation(self, instance):
        representation = \
            super(LectureListSerializer, self).to_representation(instance)
        representation['speaker'] = instance.speaker.email
        representation['event'] = instance.event.title
        return representation


class LectureDetailSerializer(serializers.ModelSerializer):
    """ Lecture Serializer for detail in admin console """

    class Meta:
        model = Lecture
        fields = ('id', 'class_room', 'speaker', 'event', 'enable')
