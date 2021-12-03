from django.db import models

from base.models import BaseModel
from .product import Product


class Item(BaseModel):
    quantity    = models.PositiveIntegerField(default=1)                                                                        # noqa E221
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)                                                          # noqa E221

    @property
    def price(self):
        product_price = self.product.discounted_price
        return self.quantity * product_price

    @staticmethod
    def create_item(product_id, quantity):
        product = Product.objects.get(id=product_id)
        item = Item(product=product, quantity=quantity)
        item.save()
        return item

    def __str__(self):
        return f"{self.quantity} of {self.product}"
