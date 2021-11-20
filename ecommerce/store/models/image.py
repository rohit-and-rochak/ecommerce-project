from django.db import models

from base.models import BaseModel


class Image(BaseModel):
    default = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='items')

    def __str__(self):
        return f"Image: {self.name}"

    @property
    def get_url(self):
        return self.image.url
