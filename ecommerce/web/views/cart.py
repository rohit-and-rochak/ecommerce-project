from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render

from base.constants import STATE_CHOICES
from base.models import User
from store.models import Cart


@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    total_price = 0
    discount = 0
    cart_items = []
    if cart:
        cart_items = cart.items.all()
        total_price = cart.total_price
        discount = total_price - cart.discounted_price

    return render(request, 'cart.html', {'cart_items': cart_items, 'sub_total': total_price, 'discount': discount})


@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    total_price = 0
    discount = 0
    if cart:
        total_price = cart.total_price
        discount = total_price - cart.discounted_price

    return render(request, 'checkout.html', {'sub_total': total_price, 'discount': discount, 'states': STATE_CHOICES})


@require_POST
def add_to_cart(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login to add products'}, status=500)

    if request.is_ajax:
        try:
            cart, _ = Cart.objects.get_or_create(user=request.user)
            data = request.POST
            product_id = data.get('product_id')
            quantity = int(data.get('quantity'))
            cart.add_item(product_id, quantity)
            return JsonResponse({'data': None}, status=200)
        except Exception as e:
            print(e)

    return JsonResponse({'error': 'Could not add item to cart'}, status=500)


@require_POST
def remove_from_cart(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized request'}, status=500)

    if request.is_ajax:
        cart = Cart.objects.get(user=request.user)
        data = request.POST
        product_id = data.get('product_id')
        item = cart.items.all().filter(product_id=product_id).first()
        if item:
            quantity = data.get('quantity')
            if quantity:
                quantity = int(quantity)
            else:
                quantity = item.quantity

            cart.remove_item(product_id, quantity)
            return JsonResponse({'data': None}, status=200)

    return JsonResponse({'error': 'invalid request'}, status=500)


@require_POST
def change_quantity(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized request'}, status=500)

    if request.is_ajax:
        cart = Cart.objects.get(user=request.user)
        data = request.POST
        product_id = data.get('product_id')
        item = cart.items.all().filter(product_id=product_id).first()
        if item:
            quantity = int(data.get('quantity'))
            item.quantity = quantity
            item.save()

            return JsonResponse({'data': None}, status=200)

    return JsonResponse({'error': 'Could not change quantity'}, status=500)


@require_POST
def place_order(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized requests'}, status=500)

    if request.is_ajax:
        user_keys = ['first_name', 'last_name', 'phone', 'email']
        address_keys = ['country', 'state', 'raw-address', 'pincode']
        data = request.POST

        user = User()
        for key in user_keys:
            setattr(user, key, data.get(key))

        user.save()



        return JsonResponse({'data': None}, status=200)

    return JsonResponse({'error': 'Could not place order'}, status=500)
