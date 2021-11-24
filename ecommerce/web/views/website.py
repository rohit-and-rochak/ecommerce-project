from django.contrib.auth import logout
from django.shortcuts import render, redirect

from base.constants import STATE_CHOICES
from store.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def shop(request):
    return render(request, 'shop.html')


def about(request):
    return render(request, 'about.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def product(request, pk):
    product = Product.objects.get(id=pk)
    all_products = Product.objects.all().exclude(id=pk)
    return render(request, 'product.html', {'product': product, 'all_products': all_products})


def profile(request):
    return render(request, 'account/profile.html', {'states': STATE_CHOICES})


def logout_user(request):
    logout(request)
    redirect_url = '/login/'
    response = redirect(redirect_url)

    if not request.user.is_authenticated:
        for cookie in request.COOKIES:
            response.delete_cookie(cookie)
        request.session.flush()

    return response
