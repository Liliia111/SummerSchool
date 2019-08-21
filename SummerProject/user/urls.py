# pylint: disable=C0103
"""Url for user app"""

from django.urls import path
from .views import registration, login, logout, UserView

urlpatterns = [
    path('registration/', registration),
    path('login/', login),
    path('logout/', logout),
    path('self/', UserView.as_view())
]
