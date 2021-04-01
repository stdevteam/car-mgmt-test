from django.db import models
from django.utils import timezone


class AbstractDateTime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True