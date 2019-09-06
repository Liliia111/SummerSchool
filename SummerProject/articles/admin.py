from django.contrib import admin
from articles.models import Article, Comment
from categories.models import Category, Team
from user.models import User, Role


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Team)
admin.site.register(User)
admin.site.register(Role)