from django.db import models

from base.models import BaseModel
from .item import Item


class Image(BaseModel):
    default = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image: {self.name}"
