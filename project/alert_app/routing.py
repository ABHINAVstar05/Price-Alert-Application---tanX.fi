from django.urls import path

from .socket_connection import get_prices

websocket_urlpatterns = [
    path('ws/real-time-data/', get_prices),
]