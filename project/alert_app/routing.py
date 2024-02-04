from django.urls import re_path

from .socket_connection import *

# routing.py

websocket_urlpatterns = [
    re_path(r'ws/binance/$', main),
]
