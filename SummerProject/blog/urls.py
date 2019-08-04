from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>', views.ArticleDetail.as_view()),
]