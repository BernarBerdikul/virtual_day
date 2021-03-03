from rest_framework import serializers
from virtual_day.core.models import Billboard
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils import constants


class BillboardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Billboard
        fields = ('id', 'title', 'period_start', 'period_end', 'created_at')

    def to_representation(self, instance):
        representation = super(BillboardListSerializer, self).to_representation(instance)
        representation['created_at'] = instance.created_at.strftime(
            f'%d {constants.MONTHS[int(instance.created_at.strftime("%m")) - 1][2]} %Y %H:%M')
        return representation


class BillboardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billboard
        fields = ('id', 'title', 'description', 'image', 'created_at')

    def to_representation(self, instance):
        representation = super(BillboardDetailSerializer, self).to_representation(instance)
        if instance.type == constants.TEXT:
            representation['image'] = get_full_url(instance.image)
            representation['description'] = instance.description
        elif instance.type == constants.VIDEO:
            representation['url_link'] = instance.url_link
        representation['created_at'] = instance.created_at.strftime(
            f'%d {constants.MONTHS[int(instance.created_at.strftime("%m")) - 1][2]} %Y %H:%M')
        return representation
