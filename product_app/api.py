from .models import Item_transfer, Commodity, Product, Store, Item_transfer_type
from rest_framework import viewsets, permissions, generics
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


class ItemTransfersViewSet(viewsets.ModelViewSet):
    # Item transfer viewset
    queryset = Item_transfer.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = ItemTransfersSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProductsViewSet(viewsets.ModelViewSet):
    # Commodities viewset
    queryset = Product.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = ProductsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CommoditiesViewSet(viewsets.ModelViewSet):
    # Commodities viewset
    queryset = Commodity.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = CommoditiesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class BalancesViewSet(viewsets.ModelViewSet):
    # Commodities viewset
    queryset = Item_balance.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = BalancesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class StoresViewSet(viewsets.ModelViewSet):
    # Commodities viewset
    queryset = Store.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = StoresSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class TransferTypesViewSet(viewsets.ModelViewSet):
    # Commodities viewset
    queryset = Item_transfer_type.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = TransferTypesSerializer
    authentication_classes = (TokenAuthentication,)

    permission_classes = (IsAuthenticated,)


class ClientProductsViewSet(generics.ListAPIView):
    #queryset = Item_balance.objects.filter().all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = ClientItemsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        client = self.kwargs['client']
        return Item_balance.objects.filter(client=client, product__isnull=False).exclude(quantity=0)


class ClientCommoditiesViewSet(generics.ListAPIView):
    #queryset = Item_balance.objects.filter().all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = ClientItemsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        client = self.kwargs['client']
        return Item_balance.objects.filter(client=client, commodity__isnull=False).exclude(quantity=0, size=0)


class UserProductsViewSet(generics.ListAPIView):
    #queryset = Item_balance.objects.filter().all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = ClientItemsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user = self.kwargs['user']
        return Item_balance.objects.filter(user=user, product__isnull=False).exclude(quantity=0)


class UserCommoditiesViewSet(generics.ListAPIView):
    #queryset = Item_balance.objects.filter().all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = ClientItemsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.kwargs['user']
        return Item_balance.objects.filter(user=user, commodity__isnull=False)


class DivisionItemBalancesViewSet(generics.ListAPIView):
    #queryset = Item_balance.objects.filter().all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = DivisionItemBalancesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        division = self.kwargs['division']
        return Item_balance.objects.filter(division=division)
