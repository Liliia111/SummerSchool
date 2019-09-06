from django.urls import path
from django.contrib import admin
from articles import views


urlpatterns = [
    path('<int:pk>/', views.ArticleDetailView.as_view()),
    path('admin/', admin.site.urls),
]