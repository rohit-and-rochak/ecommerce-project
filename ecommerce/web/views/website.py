from django.shortcuts import render
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
