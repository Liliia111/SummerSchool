from django.urls import path, include
from .views import registration, login, logout, UserView


urlpatterns = [
    path('registration/', registration),
    path('login/', login),
    path('logout/', logout),
    path('update_info/', UserView.as_view())
]
