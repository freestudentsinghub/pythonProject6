from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import AllowAny

from users.models import Payments, CustomUser
from users.serliazers import PaymentsSerializers, CustomUserSerializer


# Create your views here.

class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentsSerializers
    queryset = Payments.objects.all()
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['paid_course', 'separately_paid_lesson', 'payment_method']
    ordering_fields = ['payment_date']


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()