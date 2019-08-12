from django.urls import path, include
from .views import registration, login, logout


urlpatterns = [
    path('registration/', registration),
    path('login/', login),
    path('logout/', logout)
]
