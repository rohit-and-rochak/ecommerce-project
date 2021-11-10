from rest_framework.viewsets import ModelViewSet

from base.api import BaseSerializer
from ..models import Order


class OrderSerializer(BaseSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
