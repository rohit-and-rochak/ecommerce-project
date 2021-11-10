from rest_framework.routers import SimpleRouter

from .api import ItemViewSet, OrderViewSet, TransactionViewSet


router = SimpleRouter()
router.register('items', ItemViewSet, basename='items')
router.register('orders', OrderViewSet, basename='orders')
router.register('transactions', TransactionViewSet, basename='transactions')
