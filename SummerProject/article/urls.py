from django.urls import path
from .views import Article_V, ArticleDetail
app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', Article_V.as_view()),
    path('articles/<int:id>', ArticleDetail.as_view())
]