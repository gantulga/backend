from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from product_app import views
from rest_framework import routers
from hotel.api import HotelClientLogsViewSet, HotelRoomsViewSet, HotelOrdersViewSet, HotelOrdersViewSet2, HotelOrdersViewSet3, HotelOrdersViewSet4, HotelOrderDetialsViewSet, HotelPaymentsViewSet, HotelProductsViewSet, HotelOrderDetialsViewSet2, UnderpaymentsViewSet, HotelOrdersNewHotelViewSet, BeforeReceivablesViewSet, ShiftOrdersViewSet, ShiftPaymentsViewSet
from product_app.api import ItemTransfersViewSet, CommoditiesViewSet, ProductsViewSet, StoresViewSet, TransferTypesViewSet, ClientProductsViewSet, ClientCommoditiesViewSet, UserProductsViewSet, UserCommoditiesViewSet, BalancesViewSet, DivisionItemBalancesViewSet
from structure_app.api import SettingsViewSet, CustomersViewSet, UsersViewSet, DivisionsViewSet, ClientsViewSet, DivisionClientsViewSet, ShiftWorksViewSet, LastShiftWorkViewSet
from financial_app.api import FinanceWalletsViewSet, BudgetsViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('hotel/clientlogs', HotelClientLogsViewSet, 'clientlogs')
router.register('hotel/rooms', HotelRoomsViewSet, 'rooms')
router.register('hotel/orders', HotelOrdersViewSet, 'hotelOrders')
router.register('hotel/newRoomOrder',
                HotelOrdersNewHotelViewSet, 'newRoomOrder')
router.register('hotel/underpayments',
                UnderpaymentsViewSet, 'hotelUnderpayments')
router.register('hotel/beforereceivables',
                BeforeReceivablesViewSet, 'beforereceivables')
router.register('hotel/workshiftorders',
                ShiftOrdersViewSet, 'workshiftorders')
router.register('hotel/workshiftpayments',
                ShiftPaymentsViewSet, 'workshiftpayments')
router.register('hotel/orders2', HotelOrdersViewSet4, 'hotelOrders2')
router.register('hotel/ordersForPayments',
                HotelOrdersViewSet2, 'ordersForPayments')
router.register('hotel/ordersDetials',
                HotelOrderDetialsViewSet, 'hotelOrdersDetials')
router.register('hotel/ordersDetials2',
                HotelOrderDetialsViewSet2, 'hotelOrdersDetials2')
router.register('hotel/products', HotelProductsViewSet, 'hotelProducts')
router.register('hotel/payments', HotelPaymentsViewSet, 'hotelPayments')
router.register('hotel/shiftWorks', ShiftWorksViewSet, 'shiftWorks')

router.register('item/transfers', ItemTransfersViewSet, 'itemTransfers')
router.register('item/commodities', CommoditiesViewSet, 'commodities')
router.register('item/products', ProductsViewSet, 'products')
router.register('item/balances', BalancesViewSet, 'balances')
router.register('item/transfers', ItemTransfersViewSet, 'itemTransfers')
router.register('item/transferTypes', TransferTypesViewSet, 'transferTypes')

router.register('settings', SettingsViewSet, 'settings')
router.register('finance/wallets', FinanceWalletsViewSet, 'wallets')
router.register('finance/budgets', BudgetsViewSet, 'budgets')
router.register('customers', CustomersViewSet, 'customers')
router.register('users', UsersViewSet, 'users')
router.register('divisions', DivisionsViewSet, 'divisions')
router.register('clients', ClientsViewSet, 'clients')
router.register('stores', StoresViewSet, 'stores')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hotel/', include('hotel.urls')),
    path('api/', include(router.urls)),
    path('generate_token/', views.obtain_auth_token, name='generate_token'),
    url('^api/hotel/ordersForClients/(?P<client>.+)/$',
        HotelOrdersViewSet3.as_view()),

    url('^api/client/(?P<client>.+)/products/$',
        ClientProductsViewSet.as_view()),
    url('^api/client/(?P<client>.+)/commodities/$',
        ClientCommoditiesViewSet.as_view()),

    url('^api/user/(?P<user>.+)/products/$',
        UserProductsViewSet.as_view()),
    url('^api/user/(?P<user>.+)/commodities/$',
        UserCommoditiesViewSet.as_view()),

    url('^api/division=(?P<division>.+)/clients/$',
        DivisionClientsViewSet.as_view()),

    url('^api/division=(?P<division>.+)/item/balances/$',
        DivisionItemBalancesViewSet.as_view()),

    url('^api/hotel/shiftWorks/last$', LastShiftWorkViewSet.as_view()),
    # path('product/', include('product_app.urls')),
    # path('basic_asset/', views.Basic_asset_function, name='Basic_asset'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
