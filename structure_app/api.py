from .models import Configuration_value, Customer
from rest_framework import viewsets, permissions
from .serializers import SettingsSerializer, CustomersSerializer, UsersSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


# Settings Viewset
class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Configuration_value.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = SettingsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

# Customers Viewset


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = CustomersSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
