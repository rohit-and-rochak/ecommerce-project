from rest_framework.routers import SimpleRouter

from .api import ItemViewSet


router = SimpleRouter()
router.register('items', ItemViewSet, basename='items')
