from decimal import Decimal

from django.db import models

from base.models import BaseModel, Address, User
from .cart import Cart


class Order(BaseModel):
    class Delievery(models.TextChoices):
        DELIEVERY = 'DELIEVERY'
        PICKUP = 'PICKUP'

    class Status(models.TextChoices):
        PENDING   = 'PENDING'   # noqa E221
        PLACED    = 'PLACED'    # noqa E221
        CANCELLED = 'CANCELLED' # noqa E221
        COMPLETED = 'COMPLETED' # noqa E221

    address   = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)                                                        # noqa E221
    delievery = models.CharField(max_length=20, choices=Delievery.choices, default=Delievery.DELIEVERY, null=False, blank=True)    # noqa E221
    cart      = models.OneToOneField(Cart, on_delete=models.CASCADE)                                                                                            # noqa E221
    status    = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, null=False, blank=True)                 # noqa E221
    customer  = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)                                             # noqa E221

    def __str__(self):
        return f"{self.delievery.lower()} order for {self.user}"

    def get_order_amount(self):
        items = self.items.all()
        total_amount = sum([item.get_price() for item in items])
        discount_factor = Decimal(1 - self.discount/100)

        return round(total_amount * discount_factor, 2)
