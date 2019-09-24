from django.conf.urls import url
from django.urls import path
from .views import ArticleDetailView, comments_view, most_commented, MostPopularView, more_articles, more_articles_2

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view()),
    path('<int:article_id>/comments/', comments_view),
    path('most_commented/', most_commented),
    path('more_articles/', more_articles),
    path('more_articles_2/', more_articles_2),
    path('most_popular/', MostPopularView.as_view(), name='most_popular'),
    path('most_commented/', most_commented),
]