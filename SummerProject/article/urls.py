""" Urls for articles """
from django.urls import path
from .views import comments_view

urlpatterns = [
    path('<int:article_id>/comments/', comments_view),
]
