from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155, blank=False)
    parent_category_id = models.ForeignKey("self", on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
