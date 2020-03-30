from .models import Order, Order_detial, Order_payments, Payment
from rest_framework import viewsets, permissions
from .serializers import OrdersSerializer, OrderDetialsSerializer, PaymentsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django_filters import rest_framework as filters
import datetime


# Settings Viewset
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrdersSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    depth = 1


class OrderDetialFilter(filters.FilterSet):
    fr_date_start = filters.DateTimeFilter(
        field_name="fr_date", lookup_expr='gte')
    fr_date_end = filters.DateTimeFilter(
        field_name="fr_date", lookup_expr='lte')
    to_date_start = filters.DateTimeFilter(
        field_name="to_date", lookup_expr='gte')
    to_date_end = filters.DateTimeFilter(
        field_name="to_date", lookup_expr='lte')

    class Meta:
        model = Order_detial
        fields = ['fr_date_start', 'fr_date_end',
                  'to_date_start', 'to_date_end']

    # def get_queryset(self):
    #     queryset = Order_detial.objects.all()
    #     fr_date = self.request.query_params.get('fr_date', None)
    #     to_date = self.request.query_params.get('to_date', None)
    #     if fr_date and to_date:
    #         queryset = queryset.filter(
    #             fr_date__gte=fr_date, fr_date__lte=to_date)
    #        # queryset = queryset.filter(fr_date__range[fr_date, to_date])
    #     return queryset


class OrderDetialsViewSet(viewsets.ModelViewSet):
    queryset = Order_detial.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderDetialsSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderDetialFilter


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentsSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
