""" Urls for articles """
from django.urls import path
from .views import comment_form

urlpatterns = [
    path('<int:article_id>/comment/', comment_form),
]
