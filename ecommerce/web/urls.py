from django.urls import path

from .views import website

urlpatterns = [
    path('', website.home, name='home'),
    path('shop/', website.shop, name='shop'),
    path('about/', website.about, name='about'),
    path('cart/', website.cart, name='cart'),
    path('checkout/', website.checkout, name='checkout'),
    path('product/<uuid:pk>/', website.product, name='product'),
    path('logout/', website.logout_user, name="logout"),
    path('profile/', website.profile, name="profile"),

]
