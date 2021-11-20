from django.urls import path

from .views import website

urlpatterns = [
    path('', website.home, name='home'),
    path('shop/', website.shop, name='shop'),
    path('about/', website.about, name='about'),
    path('cart/', website.cart, name='cart'),
    path('checkout/', website.checkout, name='checkout'),
    path('item/<uuid:pk>/', website.item, name='item')
]
