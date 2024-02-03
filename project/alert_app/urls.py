from django.urls import path

from .auth_view import *
from .api_views import *

urlpatterns = [

    # Auth urls to show JWT Auth.
    path('signup/', signup),
    path('login/', login),

    # Alert api urls.
    path('create/', create),
    path('delete/', delete),
    path('fetch/', fetch),
]
