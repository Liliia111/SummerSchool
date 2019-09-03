from django.urls import path
from django.contrib import admin
from articles import views

app_name = "articles"
urlpatterns = [
    path('<int:pk>/', views.ArticleDetailView.as_view()),
    path('admin/', admin.site.urls),
]