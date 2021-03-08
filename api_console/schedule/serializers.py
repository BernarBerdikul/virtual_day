from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from translations.models import Translation
from business_service.translation_service_serializer import TranslationScheduleSerializer
from virtual_day.core.models import Schedule, Billboard


class BillboardShortListSerializer(serializers.ModelSerializer):
    """ Billboard serializer for select in front """
    value = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()

    class Meta:
        model = Billboard
        fields = ('value', 'label',)

    def get_value(self, obj):
        return obj.id

    def get_label(self, obj):
        return obj.title


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
    translations = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ('id', 'period_start', 'period_end',
                  'billboard', 'speaker_id', 'translations',)

    def to_representation(self, instance):
        representation = super(ScheduleDetailSerializer, self).to_representation(instance)
        return representation

    def get_translations(self, obj):
        """ return translations fields from model Translation for event """
        model_type_id = ContentType.objects.get_for_model(Schedule).id
        translations = Translation.objects.filter(object_id=obj.id, content_type_id=model_type_id).distinct('language')
        return TranslationScheduleSerializer(translations, many=True,
                                             context={"model_type_id": model_type_id}).data
