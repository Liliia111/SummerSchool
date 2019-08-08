from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=False)

    def __str__(self):
        return '%s %s' % (self.title, self.content)
