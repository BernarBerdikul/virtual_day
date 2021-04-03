from rest_framework import serializers
from virtual_day.core.models import Schedule
from virtual_day.users.models import User


class ScheduleListSerializer(serializers.ModelSerializer):
    """ Schedule serializer for short information in list """

    class Meta:
        model = Schedule
        fields = ('id', 'period_start', 'period_end', 'event')

    def to_representation(self, instance):
        representation = super(
            ScheduleListSerializer, self).to_representation(instance)
        if instance.speaker_id is not None:
            representation['speaker'] = \
                User.objects.get(id=instance.speaker_id).first_name
        else:
            representation['speaker'] = None
        return representation


class ScheduleDetailSerializer(serializers.ModelSerializer):
    """ Schedule serializer for detail information """

    class Meta:
        model = Schedule
        fields = ('id', 'period_start', 'period_end', 'event', 'speaker_id', 'billboard')

    def to_representation(self, instance):
        representation = super(ScheduleDetailSerializer, self).to_representation(instance)
        return representation
