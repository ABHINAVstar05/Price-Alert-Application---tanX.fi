from django.urls import path

from .auth_view import *

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
]