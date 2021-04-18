from rest_framework import serializers
from virtual_day.core.models import Event, Billboard
from virtual_day.users.models import User


class EventListSerializer(serializers.ModelSerializer):
    """ Event serializer for short information in list """

    class Meta:
        model = Event
        fields = ('id', 'period_start', 'period_end', 'title')

    def to_representation(self, instance):
        representation = super(
            EventListSerializer, self).to_representation(instance)
        return representation


class EventDetailSerializer(serializers.ModelSerializer):
    """ Schedule serializer for detail information """

    class Meta:
        model = Event
        fields = ('id', 'period_start', 'period_end', 'title',)

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
