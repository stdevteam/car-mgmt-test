from django.conf.urls import url
from django.urls import include

urlpatterns = [url(r'api/customers', include('api.customers.urls')),]