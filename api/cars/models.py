from django.db import models

from api.cars.enums import SEATS, TRANSMISSION, CATEGORIES
from api.core.manager import AbstractDateTime


class Car(AbstractDateTime):
    mark = models.CharField(max_length=255)
    color = models.CharField(max_length=255, null=True)
    year = models.DateField(null=True)
    engine = models.CharField(max_length=255, null=True)
    seats = models.CharField(max_length=32, choices=SEATS, null=True)
    transmission = models.CharField(max_length=32, choices=TRANSMISSION)
    categories = models.CharField(max_length=32, choices=CATEGORIES)

    def __str__(self):
        return self.mark

    class Meta:
        db_table = 'car'
