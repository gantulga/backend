from rest_framework import serializers
from .models import Wallet, Budget

# Settings Serializer


class FinanceWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class BudgetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
