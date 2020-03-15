from django.urls import path
from django.conf.urls import pattern, urls

urlpatterns = [
    url(r'^show/(?P<notification_id>\d+)/$', 'show_notification'),
    url(r'^delete/(?P<notification_id>\d+)/$', 'delete_notification'),
]
