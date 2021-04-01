from rest_framework import viewsets

from api.customers.models import Customer
from api.customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
