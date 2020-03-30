from rest_framework import serializers
from .models import Configuration_value, Customer
from django.contrib.auth.models import User

# Settings Serializer


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration_value
        fields = '__all__'


class CustomersSerializer(serializers.ModelSerializer):
    mobile = serializers.IntegerField(
        required=False, allow_null=True)
    email = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)
    address = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = Customer
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
