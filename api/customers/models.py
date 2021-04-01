from django.db import models

from api.core.manager import AbstractDateTime

class Customer(AbstractDateTime):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    last_booking = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'customer'
