from hotel.models import Hotel_client_log
from structure_app.models import Client
from rest_framework import viewsets, permissions
from .serializers import HotelClientLogsSerializer, HotelRoomsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Hotel_client_log Viewset
class HotelClientLogsViewSet(viewsets.ModelViewSet):
    queryset = Hotel_client_log.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = HotelClientLogsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HotelRoomsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(
        division=3, number__range=(200, 308)).all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = HotelRoomsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
