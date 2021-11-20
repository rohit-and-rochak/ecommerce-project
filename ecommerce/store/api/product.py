from rest_framework.viewsets import ModelViewSet

from base.api import BaseSerializer
from ..models import Product


class ProductSerializer(BaseSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
