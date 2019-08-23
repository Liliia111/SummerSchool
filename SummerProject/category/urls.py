from django.urls import path, include
from .views import categories


urlpatterns = [
    path('', categories),

]
