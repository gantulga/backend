from rest_framework import serializers
from .models import Wallet

# Settings Serializer


class FinanceWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'
