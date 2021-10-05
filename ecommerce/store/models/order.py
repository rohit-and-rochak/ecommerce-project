from django.db import models

from address.models import AddressField

from base.models import BaseModel, User


class Order(BaseModel):
    class Delievery(models.TextChoices):
        HOME_DELIEVERY = 'HOME_DELIEVERY'
        PICKUP = 'PICKUP'

    class Status(models.TextChoices):
        PENDING   = 'PENDING'   # noqa E221
        PLACED    = 'PLACED'    # noqa E221
        CANCELLED = 'CANCELLED' # noqa E221
        COMPLETED = 'COMPLETED' # noqa E221

    address   = AddressField()                                                                                                          # noqa E221
    delievery = models.CharField(max_length=20, choices=Delievery.choices, default=Delievery.HOME_DELIEVERY, null=False, blank=True)    # noqa E221
    discount  = models.PositiveSmallIntegerField(default=0)                                                                             # noqa E221
    status    = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, null=False, blank=True)                 # noqa E221
    user      = models.ForeignKey(User, on_delete=models.DO_NOTHING)                                                                    # noqa E221
