from django.contrib import admin

from .models import Image, Product, Order, Transaction, Item


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'delievery', 'status')


admin.site.register(Image)
admin.site.register(Item)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Transaction)
