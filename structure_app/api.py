from .models import Configuration_value, Customer, Division, Client
from rest_framework import viewsets, permissions, generics
from .serializers import SettingsSerializer, CustomersSerializer, UsersSerializer, DivisionsSerializer, ClientsSerializer
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
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)


class DivisionsViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = DivisionsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientsSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)


class DivisionClientsViewSet(generics.ListAPIView):
    #queryset = Item_balance.objects.filter().all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientsSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        division = self.kwargs['division']
        return Client.objects.filter(division=division)
