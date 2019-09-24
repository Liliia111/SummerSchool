from django.urls import path
from django.contrib import admin
from articles.views import *


urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view()),
    path('admin/', admin.site.urls),
    path('<int:article_id>/comments/', comments_view),
    path('most_commented/', most_commented),
    path('more_articles/', more_articles),
    path('more_articles_2/', more_articles_2),
]