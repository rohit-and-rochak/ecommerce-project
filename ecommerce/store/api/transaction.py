from rest_framework.viewsets import ModelViewSet

from base.api import BaseSerializer
from ..models import Transaction


class TransactionSerializer(BaseSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all().order_by('-created_at')
    serializer_class = TransactionSerializer
