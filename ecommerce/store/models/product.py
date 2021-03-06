from decimal import Decimal

from django.db import models

from base.models import BaseModel
from .image import Image


class Product(BaseModel):
    class Category(models.TextChoices):
        DAIRY = 'DAIRY'
        BREADS = 'BREADS'
        OILS = 'OILS'
        CREAMS = 'CREAMS'

    class Unit(models.TextChoices):
        Kg = 'Kg'
        Gm = 'Gm'
        Units = 'Units'
        L = 'L'

    name        = models.CharField(max_length=100)                                                                              # noqa E221
    category    = models.CharField(max_length=20, choices=Category.choices, default=Category.DAIRY, null=False, blank=True)   # noqa E221
    description = models.TextField(max_length=500, blank=True, null=True)                                                       # noqa E221
    discount    = models.PositiveSmallIntegerField(default=0, null=False, blank=True)                                           # noqa E221
    price       = models.DecimalField(max_digits=10, decimal_places=2)                                                          # noqa E221
    quantity    = models.PositiveIntegerField(default=1)                                                                        # noqa E221
    image       = models.OneToOneField(Image, on_delete=models.CASCADE)                                              # noqa E221
    units       = models.CharField(max_length=10, choices=Unit.choices, default=Unit.Units)                                       # noqa E221
    featured    = models.BooleanField(default=False)                                       # noqa E221

    def __str__(self):
        return f"{self.name} @ {self.price}"

    @property
    def discounted_price(self):
        discount_factor = Decimal(1-self.discount/100)
        return round(self.price * discount_factor, 2)
