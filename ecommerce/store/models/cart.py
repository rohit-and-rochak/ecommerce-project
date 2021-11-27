from django.db import models

from base.models import BaseModel, User
from .item import Item


class Cart(BaseModel):
    items     = models.ManyToManyField(Item)                                                                                            # noqa E221
    user      = models.ForeignKey(User, on_delete=models.CASCADE)                                                                       # noqa E221

    def add_item(self, product_id, quantity):
        item = self.items.all().filter(product__id=product_id).first()
        if item:
            item.quantity += quantity
            item.save()
        else:
            item = Item.create_item(product_id, quantity)
            self.items.add(item)
            self.save()

        item.product.quantity -= quantity
        item.product.save()

    def remove_item(self, product_id, quantity):
        item = self.items.all().filter(product__id=product_id).first()
        if item:
            if item.quantity == quantity:
                item.delete()
            else:
                item.quantity -= quantity
                item.save()

        item.product.quantity += quantity
        item.product.save()

    @property
    def total_price(self):
        items = self.items.all()
        return sum([item.product.discounted_price*item.quantity for item in items])
