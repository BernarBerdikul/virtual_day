from rest_framework import serializers
from virtual_day.core.models import Billboard, MediaBillboard
from virtual_day.utils.image_utils import get_full_url
from virtual_day.utils import constants


class BillboardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billboard
        fields = ('id', 'title', 'description', 'image',
                  'unique_key', 'type', 'enable',)

    def to_representation(self, instance):
        representation = super(
            BillboardDetailSerializer, self).to_representation(instance)
        representation['type'] = constants.BILLBOARD_TYPES[instance.type][1]
        representation['image'] = get_full_url(instance.image)
        representation['unique_key'] = \
            constants.UNIQUE_KEY_FOR_BILLBOARD[instance.unique_key][1]
        static_billboard = MediaBillboard.objects.get(
            billboard_id=instance.id,
            language=self.context['language'])
        if static_billboard.pdf_file != '':
            representation['pdf_file'] = None
        elif static_billboard.url_link is not None:
            representation['url_link'] = static_billboard.url_link
        return representation
