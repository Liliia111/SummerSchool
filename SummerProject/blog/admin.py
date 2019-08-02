from django.contrib import admin
# the module name is app_name.models
from .models import Article

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Article)
