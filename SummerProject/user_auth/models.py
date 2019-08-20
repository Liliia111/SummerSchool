from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

from enum import Enum

class SocialNetworkChoice(Enum):
    FB = "Facebook"
    TR = "Twitter"
    GGL = "Google"
class Role(models.Model):
    role = models.CharField(max_length=254)

    def __str__(self):
        return self.role


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, blank=True)
    password = models.CharField(max_length=10000, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    @staticmethod
    def create(first_name, last_name, email, password, role):
        user = User(first_name=first_name, last_name=last_name, email=email, role=role)
        user.set_password(password)
        user.save()
        return user

    def update(self, first_name=None, last_name=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name

        self.save()



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
    team = models.ForeignKey(Team)
    category = models.ForeignKey(Category)

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey(User)

class ArticleComment(Article, Comment):
    article = models.ForeignKey(Article)
    comment = models.ForeignKey(Comment)