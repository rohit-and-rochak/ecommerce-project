from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect

from base.constants import STATE_CHOICES
from store.models import Product


def home(request):
    products = Product.objects.filter(featured=True)
    return render(request, 'home.html', {'products': products})


def shop(request):
    all_products = Product.objects.all()
    categories = [choice[0] for choice in Product.Category.choices]
    products = {}
    for category in categories:
        products[category] = list(all_products.filter(category=category))

    return render(request, 'shop.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def product(request, product_id):
    item = Product.objects.get(id=product_id)
    products = Product.objects.all().exclude(id=product_id)
    return render(request, 'product.html', {'item': item, 'products': products})


@login_required
def profile(request):
    return render(request, 'account/profile.html', {'states': STATE_CHOICES})


@require_POST
@login_required
def update_profile(request):
    if request.is_ajax:
        user = request.user
        data = request.POST
        for key in data.keys():
            setattr(user, key, data[key])

        user.save()
        return JsonResponse({'data': None}, status=200)

    return JsonResponse({'error': 'There occurred an error'}, status=500)


@login_required
def logout_user(request):
    logout(request)
    redirect_url = '/login/'
    response = redirect(redirect_url)

    if not request.user.is_authenticated:
        for cookie in request.COOKIES:
            response.delete_cookie(cookie)
        request.session.flush()

    return response
