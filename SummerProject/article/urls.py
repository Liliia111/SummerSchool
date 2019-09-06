""" Urls for articles """
from django.urls import path
from .views import comments_view, most_commented

urlpatterns = [
    path('<int:article_id>/comments/', comments_view),
    path('most_commented/', most_commented),
]
