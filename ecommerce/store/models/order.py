from decimal import Decimal

from django.db import models

from address.models import Address

from base.models import BaseModel, User
from .item import Item


class Order(BaseModel):
    class Delievery(models.TextChoices):
        HOME_DELIEVERY = 'HOME DELIEVERY'
        PICKUP = 'PICKUP'

    class Status(models.TextChoices):
        PENDING   = 'PENDING'   # noqa E221
        PLACED    = 'PLACED'    # noqa E221
        CANCELLED = 'CANCELLED' # noqa E221
        COMPLETED = 'COMPLETED' # noqa E221

    address   = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)                                                                                      # noqa E221
    delievery = models.CharField(max_length=20, choices=Delievery.choices, default=Delievery.HOME_DELIEVERY, null=False, blank=True)    # noqa E221
    discount  = models.PositiveSmallIntegerField(default=0, null=False, blank=True)                                                                             # noqa E221
    items      = models.ManyToManyField(Item)                                                                                            # noqa E221
    status    = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, null=False, blank=True)                 # noqa E221
    user      = models.ForeignKey(User, on_delete=models.CASCADE)                                                                    # noqa E221

    def __str__(self):
        return f"{self.delievery.lower()} order for {self.user}"

    def get_order_amount(self):
        items = self.items.all()
        total_amount = sum([item.get_price() for item in items])
        discount_factor = Decimal(1 - self.discount/100)

        return round(total_amount * discount_factor, 2)
