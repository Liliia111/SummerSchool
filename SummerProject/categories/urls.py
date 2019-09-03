from django.urls import path
from .views import get_categories


urlpatterns = [
    path('', get_categories),

]
