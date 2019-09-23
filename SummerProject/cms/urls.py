from django.conf.urls import url
from django.urls import path
from .views import CommentView, CmsArticleView

urlpatterns = [
    path('article/', CmsArticleView.as_view()),
    path('comment/', CommentView.as_view()),
]
