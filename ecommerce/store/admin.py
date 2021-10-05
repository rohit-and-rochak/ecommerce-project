from django.contrib import admin

from .models import Image, Item, Order, Transaction


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'units')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delievery', 'status')


admin.site.register(Image)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Transaction)
