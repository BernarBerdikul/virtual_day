from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from translations.models import Translation
from business_service.translation_service_serializer import (
    TranslationEventSerializer
)
from virtual_day.core.models import Event


class EventListSerializer(serializers.ModelSerializer):
    """ Event serializer for short information in list """

    class Meta:
        model = Event
        fields = ('id', 'period_start', 'period_end', 'title',
                  'dod_day', 'event_type')

    def to_representation(self, instance):
        representation = super(
            EventListSerializer, self).to_representation(instance)
        representation['dod_day'] = instance.dod_day.day_date
        return representation


class EventDetailSerializer(serializers.ModelSerializer):
    """ Event serializer for detail information """
    translations = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('id', 'period_start', 'period_end', 'dod_day', 'event_type',
                  'translations')

    def get_translations(self, obj):
        """ return translations fields from model Translation for event """
        model_type_id = ContentType.objects.get_for_model(Event).id
        translations = Translation.objects.filter(
            object_id=obj.id, content_type_id=model_type_id
        ).distinct('language')
        return TranslationEventSerializer(
            translations, many=True,
            context={"model_type_id": model_type_id}).data
