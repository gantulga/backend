from rest_framework import serializers
from .models import Configuration_value

# Settings Serializer


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration_value
        fields = '__all__'
