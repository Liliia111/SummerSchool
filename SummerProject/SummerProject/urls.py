"""SummerProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import index, json_test, txt_test
from rest_framework.urlpatterns import format_suffix_patterns
from articles.views import ArticleView, ArticleDetailView


urlpatterns = [
    path('', index),
    path('api/v1/articles/', ArticleView.as_view(), name="create"),
    path('api/v1/articles/<int:pk>/', ArticleDetailView.as_view(), name="details"),
    path('txt_test/', txt_test),
    path('json_test/', json_test),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)