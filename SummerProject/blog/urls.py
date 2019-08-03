from django.urls import path
from .views import ArticleView, EditArticleView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', EditArticleView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)