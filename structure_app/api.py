from .models import Configuration_value
from rest_framework import viewsets, permissions
from .serializers import SettingsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Settings Viewset
class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Configuration_value.objects.all()
    #permission_classes = [permissions.AllowAny]
    serializer_class = SettingsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
