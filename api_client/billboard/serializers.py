from rest_framework import serializers
from virtual_day.core.models import Billboard
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils import constants


class BillboardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Billboard
        fields = ('id', 'title', 'image',)

    def to_representation(self, instance):
        representation = super(BillboardListSerializer, self).to_representation(instance)
        representation['image'] = get_full_url(instance.image)
        return representation


class BillboardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billboard
        fields = ('id', 'title', 'description', 'image',
                  'is_static', 'unique_key',
                  'type', 'enable',)

    def to_representation(self, instance):
        representation = super(BillboardDetailSerializer, self).to_representation(instance)
        representation['type'] = constants.BILLBOARD_TYPES[instance.type][1]
        representation['image'] = get_full_url(instance.image)
        return representation
