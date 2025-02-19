from rest_framework.routers import DefaultRouter
from django.urls import path

from users.views import PaymentsViewSet, UserCreateAPIView

app_name = "users"

router = DefaultRouter()
router.register(r'payment', PaymentsViewSet, basename='payment')

urlpatterns = [
    path("payment/create/", UserCreateAPIView.as_view(), name="payment_create")
] + router.urls
