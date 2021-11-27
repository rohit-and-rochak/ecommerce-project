from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render

from store.models import Cart


@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    total_price = 0
    cart_items = []
    if cart:
        cart_items = cart.items.all()
        total_price = cart.total_price

    return render(request, 'cart.html', {'cart_items': cart_items, 'cart_total': total_price})


@require_POST
@login_required
def add_to_cart(request):
    if request.is_ajax:
        try:
            cart, _ = Cart.objects.get_or_create(user=request.user)
            data = request.POST
            product_id = data.get('product_id')
            quantity = int(data.get('quantity'))
            cart.add_item(product_id, quantity)
            return JsonResponse({'data': None})
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'could not add item to cart'}, status=500)

    else:
        return JsonResponse({'error': 'invalid request'}, status=500)


@require_POST
@login_required
def remove_from_cart(request):
    if request.is_ajax:
        try:
            cart, _ = Cart.objects.get_or_create(user=request.user)
            data = request.POST
            product_id = data.get('product_id')
            quantity = int(data.get('quantity'))
            cart.remove_item(product_id, quantity)
            return JsonResponse({'data': None})
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'could not add item to cart'}, status=500)

    else:
        return JsonResponse({'error': 'invalid request'}, status=500)
