from django.urls import path

from emailsend import views

urlpatterns = [
    path('', views.index, name='index'),
]