from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from translations.models import Translation
from business_service.translation_service_serializer import TranslationSerializer
from virtual_day.core.models import Billboard
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils import constants


class BillboardListSerializer(serializers.ModelSerializer):
    """ Billboard serializer for short information in list """
    class Meta:
        model = Billboard
        fields = ('id', 'title', 'image', 'type', 'enable', 'is_static')

    def to_representation(self, instance):
        representation = super(BillboardListSerializer, self).to_representation(instance)
        representation['type'] = constants.BILLBOARD_TYPES[instance.type][1]
        representation['image'] = get_full_url(instance.image)
        return representation


class BillboardDetailSerializer(serializers.ModelSerializer):
    """ Billboard serializer for detail information """
    translations = serializers.SerializerMethodField()

    class Meta:
        model = Billboard
        fields = ('id', 'image', 'is_static', 'unique_key',
                  'type', 'enable', 'translations')

    def to_representation(self, instance):
        representation = super(BillboardDetailSerializer, self).to_representation(instance)
        representation['type'] = constants.BILLBOARD_TYPES[instance.type][1]
        representation['image'] = get_full_url(instance.image)
        return representation

    def get_translations(self, obj):
        """ return translations fields from model Translation for dish """
        model_type_id = ContentType.objects.get_for_model(Billboard).id
        translations = Translation.objects.filter(object_id=obj.id, content_type_id=model_type_id).distinct('language')
        return TranslationSerializer(translations, many=True,
                                     context={"model_type_id": model_type_id}).data


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
