from django.shortcuts import render
from store.models import Item


def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def shop(request):
    return render(request, 'shop.html')


def about(request):
    return render(request, 'about.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def product_single(request):
    return render(request, 'product_single.html')
