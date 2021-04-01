from django.db import models
from django_mysql.models import EnumField

from api.cars.enums import SEATS, TRANSMISSION, CATEGORIES
from api.core.manager import AbstractDateTime


class Car(AbstractDateTime):
    mark = models.CharField(max_length=255)
    color = models.CharField(max_length=255, null=True)
    year = models.DateField(null=True)
    engine = models.CharField(max_length=255, null=True)
    seats = EnumField(choices=SEATS, null=True)
    transmission = EnumField(choices=TRANSMISSION)
    categories = EnumField(choices=CATEGORIES)

    def __str__(self):
        return self.mark

    class Meta:
        db_table = 'car'
