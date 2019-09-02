from django.db import models

from enum import Enum


class SocialNetworkChoice(Enum):
    FB = "Facebook"
    TR = "Twitter"
    GGL = "Google"


class Category(models.Model):
    name = models.CharField(max_length=155, blank=False)
    parent_category_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Team(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
