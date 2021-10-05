from django.db import models

from base.models import BaseModel
from .item import Item


class Image(BaseModel):
    name = models.CharField(max_length=100, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    default = models.BooleanField(default=False)
    image = models.ImageField(upload_to='items', blank=True, null=True)

    def __str__(self):
        return f"Image: {self.name}"
