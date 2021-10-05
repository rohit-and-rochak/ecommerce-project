from django.contrib import admin

from .models import Image, Item, Order, Transaction

admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Transaction)
