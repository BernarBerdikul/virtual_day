from rest_framework import serializers
from virtual_day.core.models import Schedule


class ScheduleListSerializer(serializers.ModelSerializer):
    """ Schedule serializer for short information in list """

    class Meta:
        model = Schedule
        fields = ('id', 'period_start', 'period_end', 'event', 'speaker_id')

    def to_representation(self, instance):
        representation = super(ScheduleListSerializer, self).to_representation(instance)
        return representation


class ScheduleDetailSerializer(serializers.ModelSerializer):
    """ Schedule serializer for detail information """

    class Meta:
        model = Schedule
        fields = ('id', 'period_start', 'period_end', 'event', 'speaker_id', 'billboard')

    def to_representation(self, instance):
        representation = super(ScheduleDetailSerializer, self).to_representation(instance)
        return representation
