from django.db import models
from user.models import User
from category_team.models import Team, Category, SocialNetworkChoice


class Article(models.Model):
    headline = models.CharField(max_length=150, blank=False)
    photo = models.URLField(max_length=150)
    video = models.URLField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=8, choices=[(tag, tag.value) for tag in SocialNetworkChoice])
    content = models.TextField(blank=False)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Article)
