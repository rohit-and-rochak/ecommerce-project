from rest_framework.routers import SimpleRouter

from .api import ProductViewSet, OrderViewSet, TransactionViewSet


router = SimpleRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('transactions', TransactionViewSet, basename='transactions')
