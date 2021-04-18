from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from translations.models import Translation
from business_service.translation_service_serializer import (
    TranslationBillBoardSerializer
)
from virtual_day.core.models import Billboard, Event
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils import constants
from virtual_day.utils.validators import validate_image


class EventSelectSerializer(serializers.ModelSerializer):
    """ Serializer for Event to create billboard in admin console """
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='title')

    class Meta:
        model = Event
        fields = ('value', 'label')


class BillboardListSerializer(serializers.ModelSerializer):
    """ Billboard serializer for short information in list """
    image = serializers.ImageField(
        max_length=None, use_url=True,
        required=False, validators=[validate_image])

    class Meta:
        model = Billboard
        fields = ('id', 'title', 'image', 'type', 'enable', 'is_static')

    def to_representation(self, instance):
        representation = super(
            BillboardListSerializer, self).to_representation(instance)
        representation['type'] = constants.BILLBOARD_TYPES[instance.type][1]
        representation['image'] = get_full_url(instance.image)
        representation['unique_key'] = \
            constants.UNIQUE_KEY_FOR_BILLBOARD[instance.unique_key][1]
        return representation


class BillboardDetailSerializer(serializers.ModelSerializer):
    """ Billboard serializer for detail information """
    translations = serializers.SerializerMethodField()

    class Meta:
        model = Billboard
        fields = ('id', 'image', 'is_static', 'unique_key',
                  'type', 'enable', 'event', 'translations')

    def to_representation(self, instance):
        representation = super(
            BillboardDetailSerializer, self).to_representation(instance)
        # representation['type'] = constants.BILLBOARD_TYPES[instance.type][1]
        representation['image'] = get_full_url(instance.image)
        # representation['unique_key'] = \
        #     constants.UNIQUE_KEY_FOR_BILLBOARD[instance.unique_key][1]
        return representation

    def get_translations(self, obj):
        """ return translations fields from model Translation for billboard """
        model_type_id = ContentType.objects.get_for_model(Billboard).id
        translations = Translation.objects.filter(
            object_id=obj.id, content_type_id=model_type_id
        ).distinct('language')
        return TranslationBillBoardSerializer(
            translations, many=True,
            context={"model_type_id": model_type_id,
                     'billboard_id': obj.id}).data


class BillboardCreateVideoSerializer(serializers.ModelSerializer):
    """ Serializer for create static or dynamic video billboard """

    class Meta:
        model = Billboard
        fields = ('url_link',)


class BillboardCreateTextSerializer(serializers.ModelSerializer):
    """ Serializer for create static or dynamic text billboard """

    class Meta:
        model = Billboard
        fields = ('pdf_file',)
