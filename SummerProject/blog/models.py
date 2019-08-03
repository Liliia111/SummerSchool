from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.title) + ", " + str(self.content)
