from .models import Wallet
from rest_framework import viewsets, permissions
from .serializers import FinanceWalletsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Settings Viewset
class FinanceWalletsViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = FinanceWalletsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
