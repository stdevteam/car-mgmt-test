from django.core.validators import MinValueValidator
from django.db import models
from django_mysql.models import EnumField

from api.bookings.enums import INVOICE_STATUS
from api.cars.models import Car
from api.core.manager import AbstractDateTime
from api.customers.models import Customer


class Booking(AbstractDateTime):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_hire = models.DateTimeField(auto_now_add=True)
    date_of_finish = models.DateTimeField()
    confirmed = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)

    def __str__(self):
        return f'start: {self.date_of_hire} finish: {self.date_of_finish}'

    class Meta:
        db_table = 'booking'


class BookingInvoice(AbstractDateTime):
    booking = models.OneToOneField(Booking, on_delete=models.SET_NULL, null=True)
    status = EnumField(choices=INVOICE_STATUS)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(1.0)])
    note = models.CharField(max_length=1024)

    class Meta:
        db_table = 'invoice'
