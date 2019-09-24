from django.db import models
from user.models import User
from categories.models import Team, Category
from djchoices import DjangoChoices, ChoiceItem

class Choices(DjangoChoices):
    google = ChoiceItem("GG")
    facebook = ChoiceItem("FB")
    twitter = ChoiceItem("TW")


class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Article(models.Model):
    headline = models.CharField(max_length=150)
    photo = models.URLField(max_length=150)
    video = models.URLField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField()
    source = models.CharField(max_length=2, choices=Choices.choices)
    content = models.TextField(blank=False)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)

