from users.models import Payments, CustomUser
from rest_framework import serializers


class PaymentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
