from django.urls import path

from .views import website, cart

urlpatterns = [
    path('', website.home, name='home'),
    path('shop/', website.shop, name='shop'),
    path('about/', website.about, name='about'),
    path('checkout/', website.checkout, name='checkout'),
    path('product/<uuid:product_id>/', website.product, name='product'),
    path('logout/', website.logout_user, name="logout"),
    path('profile/', website.profile, name="profile"),

    path('cart/', cart.cart, name='cart'),
]
