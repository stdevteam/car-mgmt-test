from rest_framework.routers import DefaultRouter

from api.customers.views import CustomerViewSet

router = DefaultRouter()

router.register(r"^", CustomerViewSet)
urlpatterns = router.urls
