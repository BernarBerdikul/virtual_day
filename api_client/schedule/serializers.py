from rest_framework import serializers
from virtual_day.core.models import Schedule, Billboard
from virtual_day.users.models import User


class ScheduleListSerializer(serializers.ModelSerializer):
    """ Schedule serializer for short information in list """

    class Meta:
        model = Schedule
        fields = ('id', 'period_start', 'period_end', 'event', 'billboard')

    def to_representation(self, instance):
        representation = super(
            ScheduleListSerializer, self).to_representation(instance)
        if instance.speaker_id is not None:
            representation['speaker'] = \
                User.objects.get(id=instance.speaker_id).first_name
        else:
            representation['speaker'] = None
        """ return billboard title """
        if instance.billboard is not None:
            representation['billboard'] = instance.billboard.title
        else:
            representation['billboard'] = None
        return representation


class ScheduleDetailSerializer(serializers.ModelSerializer):
    """ Schedule serializer for detail information """

    class Meta:
        model = Schedule
        fields = ('id', 'period_start', 'period_end', 'event', 'billboard',
                  'speaker_id')

    def to_representation(self, instance):
        representation = super(
            ScheduleDetailSerializer, self).to_representation(instance)
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
