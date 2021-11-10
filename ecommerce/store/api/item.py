from rest_framework.viewsets import ModelViewSet

from base.api import BaseSerializer
from ..models import Item


class ItemSerializer(BaseSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer
