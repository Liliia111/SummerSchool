from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.title

    
class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
