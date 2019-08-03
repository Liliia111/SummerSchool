from django.conf.urls import url
from django.urls import path
from .views import ListArticleView
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('api/v1/articles/', ListArticleView.as_view(), name='create'),
    path('api/v1/articles/<int:pk>/', views.ArticleDetail.as_view()),
]

