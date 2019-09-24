from django.urls import path
from .views import CommentView, ArticleView

urlpatterns = [
    path('article/', ArticleView.as_view()),
    path('comment/', CommentView.as_view()),
]
