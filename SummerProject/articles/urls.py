from django.urls import path
from django.contrib import admin
from articles import views
from


urlpatterns = [
    path('<int:pk>/', views.ArticleDetailView.as_view()),
    path('admin/', admin.site.urls),
    path('<int:article_id>/comments/', comments_view),
    path('most_commented/', most_commented),
]