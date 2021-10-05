from django.db import models

from base.models import BaseModel


class Item(BaseModel):
    class Category(models.TextChoices):
        DAIRY = 'DAIRY'
        FRUITS = 'FRUITS'
        DAILY_NEEDS = 'DAILY NEEDS'
        GENERIC = 'GENERIC'

    class Unit(models.TextChoices):
        KG = 'KG'
        NOS = 'NOS'
        LITRE = 'LITRE'

    name        = models.CharField(max_length=100)                                                                              # noqa E221
    category    = models.CharField(max_length=20, choices=Category.choices, default=Category.GENERIC, null=False, blank=True)  # noqa E221
    description = models.TextField(max_length=500, blank=True, default=True)                                                    # noqa E221
    discount    = models.PositiveSmallIntegerField(default=0, null=False, blank=True)                                           # noqa E221
    price       = models.DecimalField(max_digits=10, decimal_places=2)                                                          # noqa E221
    quantity    = models.DecimalField(max_digits=4, decimal_places=2, default=0)                                                # noqa E221
    units       = models.CharField(max_length=10, choices=Unit.choices, default=Unit.NOS)                                       # noqa E221
