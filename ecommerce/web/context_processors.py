from store.models import Cart


def cart_item_count(request):
    context = {'cart_count': 0}
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            context['cart_count'] = len(cart.items.all())

    return context
