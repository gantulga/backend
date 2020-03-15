from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product_app import views
from rest_framework import routers
from hotel.api import HotelClientLogsViewSet, HotelRoomsViewSet
from structure_app.api import SettingsViewSet
from financial_app.api import FinanceWalletsViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('hotel/clientlogs', HotelClientLogsViewSet, 'clientlogs')
router.register('hotel/rooms', HotelRoomsViewSet, 'rooms')
router.register('settings', SettingsViewSet, 'settings')
router.register('finance/wallets', FinanceWalletsViewSet, 'wallets')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hotel/', include('hotel.urls')),
    path('api/', include(router.urls)),
    path('generate_token/', views.obtain_auth_token, name='generate_token'),
    # path('product/', include('product_app.urls')),

    # path('basic_asset/', views.Basic_asset_function, name='Basic_asset'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
