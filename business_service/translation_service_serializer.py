from rest_framework import serializers
from translations.models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    """ Translation Serializer for create/update/get objects in Billboard model"""
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Translation
        fields = ('title', 'description', 'language',)

    def get_title(self, obj):
        title = Translation.objects.filter(object_id=obj.object_id, field='title', language=obj.language,
                                           content_type_id=self.context['model_type_id']).first()
        if title is None:
            return None
        return title.text

    def get_description(self, obj):
        description = Translation.objects.filter(object_id=obj.object_id, field='description',
                                                 language=obj.language,
                                                 content_type_id=self.context['model_type_id']).first()
        if description is None:
            return None
        return description.text


class TranslationScheduleSerializer(serializers.ModelSerializer):
    """ Translation Serializer for create/update/get objects in Schedule model """
    event = serializers.SerializerMethodField()

    class Meta:
        model = Translation
        fields = ('event', 'language',)

    def get_event(self, obj):
        event = Translation.objects.filter(object_id=obj.object_id, field='event',
                                           language=obj.language,
                                           content_type_id=self.context['model_type_id']).first()
        if event is None:
            return None
        return event.text
