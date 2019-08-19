from django.conf.urls import url
from django.urls import path, include
from .views import registration, login, logout, UserView, ResetPasswordRequestView, PasswordResetConfirmView, success

urlpatterns = [
    path('registration/', registration),
    path('login/', login),
    path('logout/', logout),
    path('update_info/', UserView.as_view()),
    path('reset_password/', ResetPasswordRequestView.as_view(), name="reset_password"),
    path('success/', success),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='password_reset_confirm')
]
