from django.conf.urls import url
from django.urls import path
from .views import CommentView

urlpatterns = [
    path('comment/', CommentView.as_view()),
]
