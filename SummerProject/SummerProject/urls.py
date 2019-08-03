from django.contrib import admin
from django.urls import path, include

# from main import views

urlpatterns = [
    path('main/', include('main.urls')),
    path('api/v1/', include('blog.urls')),
    path('admin/', admin.site.urls),
]