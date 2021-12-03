from store.models import Cart


def cart_item_count(request):
    context = {'cart_count': 0}
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            context['cart_count'] = sum([item.quantity for item in cart.items.all()])

    return context


def global_context(request):
    return {'free_delievery': 200, 'item_count': [i for i in range(1, 6)]}
