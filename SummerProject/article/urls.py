""" Urls for articles """
from django.urls import path
from .views import comment_form, viewing_comments

urlpatterns = [
    path('<int:article_id>/comment/', comment_form),
    path('<int:article_id>/comments/', viewing_comments),
]
