from django.db import models
from .user import User

from address.models import Address as django_address


class Address(django_address):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_default = models.BooleanField(default=False)
