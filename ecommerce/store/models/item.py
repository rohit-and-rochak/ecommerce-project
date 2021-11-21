from django.db import models

from base.models import BaseModel
from .product import Product


class Item(BaseModel):
    quantity    = models.PositiveIntegerField(default=1)                                                                        # noqa E221
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)                                                          # noqa E221
