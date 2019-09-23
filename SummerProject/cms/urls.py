from django.urls import path
from .views import CmsArticleView

urlpatterns = [
    path('article/', CmsArticleView.as_view()),
]
