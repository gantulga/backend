from .models import Wallet, Budget
from rest_framework import viewsets, permissions
from .serializers import FinanceWalletsSerializer, BudgetsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Settings Viewset
class FinanceWalletsViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = FinanceWalletsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class BudgetsViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = BudgetsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
