# pylint: disable=C0103
"""Url for user app"""
from django.conf.urls import url
from django.urls import path
from .views import registration, login, logout, UserView, forgot_password_email_send, forgot_password_reset_confirm

urlpatterns = [
    path('registration/', registration),
    path('login/', login),
    path('logout/', logout),
    path('self/', UserView.as_view()),
    path('forgotPassword/', forgot_password_email_send),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', forgot_password_reset_confirm)
]
