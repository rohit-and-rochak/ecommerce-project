from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
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


@login_required
def checkout(request):
    return render(request, 'checkout.html')


def product(request, product_id):
    item = Product.objects.get(id=product_id)
    products = Product.objects.all().exclude(id=product_id)
    return render(request, 'product.html', {'item': item, 'products': products})


@login_required
def profile(request):
    return render(request, 'account/profile.html', {'states': STATE_CHOICES})


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
