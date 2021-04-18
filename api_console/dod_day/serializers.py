from rest_framework import serializers
from virtual_day.core.models import DodDay


class DodDaySerializer(serializers.ModelSerializer):
    """ DodDay Serializer in admin console """

    class Meta:
        model = DodDay
        fields = ('id', 'day_date',)
