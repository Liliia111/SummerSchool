from django.db import models
from ..user_auth.models import User

from enum import Enum

class SocialNetworkChoice(Enum):
    FB = "Facebook"
    TR = "Twitter"
    GGL = "Google"

class Category(models.Model):
    name = models.CharField(max_length=155, blank=False)
    parent_category_id = models.IntegerField(blank=False)

class Team(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Article(models.Model):
    headline = models.CharField(max_length=150, blank=False)
    photo = models.ImageField(max_length=150)
    video = models.URLField(max_length=150)
    author = models.CharField(max_length=55, blank=False)
    source = models.CharField(max_length=3, choices=[(tag, tag.value) for tag in SocialNetworkChoice])
    content = models.TextField(blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ArticleComment(Article, Comment):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)