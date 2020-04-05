from rest_framework import serializers
from scratch_bling.api.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_description',
                  'item_size', 'item_cost']
