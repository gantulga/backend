from hotel.models import Hotel_client_log
from structure_app.models import Client, Shift_work
from payment_app.models import Order, Order_detial, Payment
from product_app.models import Product
from rest_framework import viewsets, permissions, generics
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


# Hotel_client_log Viewset
class HotelClientLogsViewSet(viewsets.ModelViewSet):
    queryset = Hotel_client_log.objects.all().order_by('-id')[:100]
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelClientLogsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HotelRoomsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(
        division=3, number__range=(200, 308)).all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelRoomsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HotelProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(
        division=3, client__isnull=True).all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelProductsSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HotelOrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(division=3).all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelOrdersSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HotelOrdersNewHotelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(division=3).all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HotelOrdersNewHotelSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)


class UnderpaymentsViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(
        Q(status="Төлбөр төлөгдөөгүй.") | Q(status="Төлбөр дутуу төлсөн."), division=3)
    # permission_classes = [permissions.AllowAny]
    serializer_class = UnderpaymentsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class BeforeReceivablesViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.filter(Q(status="Төлбөр төлөгдөөгүй.") | Q(status="Төлбөр дутуу төлсөн."), division=3)
    # permission_classes = [permissions.AllowAny]
    serializer_class = UnderpaymentsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        last_shift_work = Shift_work.objects.latest('id')
        queryset = Order.objects.filter(Q(status="Төлбөр төлөгдөөгүй.") | Q(
            status="Төлбөр дутуу төлсөн."), division=3).exclude(shift_work=last_shift_work)
        return queryset


class ShiftOrdersViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.filter(Q(status="Төлбөр төлөгдөөгүй.") | Q(status="Төлбөр дутуу төлсөн."), division=3)
    # permission_classes = [permissions.AllowAny]
    serializer_class = UnderpaymentsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        last_shift_work = Shift_work.objects.latest('id')
        queryset = Order.objects.filter(shift_work=last_shift_work, division=3)
        return queryset


class ShiftPaymentsViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.filter(Q(status="Төлбөр төлөгдөөгүй.") | Q(status="Төлбөр дутуу төлсөн."), division=3)
    permission_classes = [permissions.AllowAny]
    serializer_class = HotelPaymentsSerializer2
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        last_shift_work = Shift_work.objects.latest('id')
        division = Division.objects.get(pk=3)
        queryset = Payment.objects.filter(
            shift_work=last_shift_work, division=division)
        return queryset


class HotelOrdersViewSet2(viewsets.ModelViewSet):
    queryset = Order.objects.filter(division=3).all().order_by('-id')[:30]
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelOrdersSerializer2
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HotelOrdersViewSet3(generics.ListAPIView):
    #queryset = Order.objects.filter(division=3).all().order_by('-id')[:10]
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelOrdersSerializer2
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        client = self.kwargs['client']
        return Order.objects.filter(client=client).exclude(status="Хаагдсан гүйлгээ.")


class HotelOrdersViewSet4(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelOrdersSerializer3
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HotelOrderDetialFilter(filters.FilterSet):
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


class HotelOrderDetialsViewSet(viewsets.ModelViewSet):
    queryset = Order_detial.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelOrderDetialsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HotelOrderDetialFilter


class HotelOrderDetialsViewSet2(viewsets.ModelViewSet):
    queryset = Order_detial.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelOrderDetialsSerializer2
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HotelPaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = HotelPaymentsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
