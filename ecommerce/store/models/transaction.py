from django.db import models

from base.models import BaseModel
from .order import Order


class Transaction(BaseModel):
    class Status(models.TextChoices):
        CANCELLED   = 'CANCELLED'    # noqa E221
        FAILED      = 'FAILED'       # noqa E221
        PENDING     = 'PENDING'      # noqa E221
        SUCCESSFULL = 'SUCCESSFULL'  # noqa E221

    status  = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, null=False, blank=True)   # noqa E221
    amount  = models.DecimalField(max_digits=5, decimal_places=2)                               # noqa E221
    order   = models.ForeignKey(Order, on_delete=models.DO_NOTHING)                             # noqa E221

    def __str__(self):
        return f"Transaction for {self.amount} on {self.created_at} is {self.status}"
