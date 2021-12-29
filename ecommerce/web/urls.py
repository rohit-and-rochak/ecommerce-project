from django.urls import path

from .views import website, cart

urlpatterns = [
    path('', website.home, name='home'),
    path('shop/', website.shop, name='shop'),
    path('about/', website.about, name='about'),
    path('product/<uuid:product_id>/', website.product, name='product'),
    path('logout/', website.logout_user, name="logout"),
    path('profile/', website.profile, name="profile"),
    path('update_profile/', website.update_profile, name="update-profile"),

    path('cart/', cart.cart, name='cart'),
    path('checkout/', cart.checkout, name='checkout'),
    path('change-quantity/', cart.change_quantity, name="change-quantity"),
    path('add_to_cart/', cart.add_to_cart, name="add-to-cart"),
    path('remove_from_cart/', cart.remove_from_cart, name="remove-from-cart"),
    path('place_order/', cart.place_order, name='place-order'),
]
