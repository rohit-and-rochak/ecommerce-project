from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


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
