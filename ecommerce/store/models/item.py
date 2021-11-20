from decimal import Decimal

from django.db import models

from base.models import BaseModel
from .image import Image


class Item(BaseModel):
    class Category(models.TextChoices):
        DAIRY = 'DAIRY'
        FRUITS = 'FRUITS'
        DAILY_NEEDS = 'DAILY NEEDS'
        GENERIC = 'GENERIC'

    name        = models.CharField(max_length=100)                                                                              # noqa E221
    category    = models.CharField(max_length=20, choices=Category.choices, default=Category.GENERIC, null=False, blank=True)   # noqa E221
    description = models.TextField(max_length=500, blank=True, null=True)                                                       # noqa E221
    discount    = models.PositiveSmallIntegerField(default=0, null=False, blank=True)                                           # noqa E221
    price       = models.DecimalField(max_digits=10, decimal_places=2)                                                          # noqa E221
    quantity    = models.PositiveIntegerField(default=1)                                                                        # noqa E221
    image       = models.OneToOneField(Image, on_delete=models.CASCADE)                                              # noqa E221

    def __str__(self):
        return f"{self.name} @ {self.price}"

    @property
    def discounted_price(self):
        discount_factor = Decimal(1-self.discount/100)
        return round(self.price * discount_factor, 2)
