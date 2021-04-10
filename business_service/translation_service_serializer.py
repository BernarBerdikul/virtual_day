from rest_framework import serializers
from translations.models import Translation
from virtual_day.core.models import StaticBillboard


class TranslationBillBoardSerializer(serializers.ModelSerializer):
    """ Translation Serializer for create/update/get
        objects in Billboard model"""
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Translation
        fields = ('title', 'description', 'language',)

    def to_representation(self, instance):
        representation = super(
            TranslationBillBoardSerializer, self).to_representation(instance)
        static_billboard = StaticBillboard.objects.get(
            billboard_id=self.context['billboard_id'],
            language=instance.language)
        if static_billboard.pdf_file != '':
            representation['pdf_file'] = None
        elif static_billboard.url_link is not None:
            representation['url_link'] = static_billboard.url_link
        return representation

    def get_title(self, obj):
        title = Translation.objects.filter(
            object_id=obj.object_id, field='title', language=obj.language,
            content_type_id=self.context['model_type_id']).first()
        if title is None:
            return None
        return title.text

    def get_description(self, obj):
        description = Translation.objects.filter(
            object_id=obj.object_id, field='description', language=obj.language,
            content_type_id=self.context['model_type_id']).first()
        if description is None:
            return None
        return description.text


class TranslationScheduleSerializer(serializers.ModelSerializer):
    """ Translation Serializer for create/update/get
        objects in Schedule model """
    event = serializers.SerializerMethodField()

    class Meta:
        model = Translation
        fields = ('event', 'language',)

    def get_event(self, obj):
        event = Translation.objects.filter(
            object_id=obj.object_id, field='event', language=obj.language,
            content_type_id=self.context['model_type_id']).first()
        if event is None:
            return None
        return event.text
