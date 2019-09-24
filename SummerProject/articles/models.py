from django.db import models
from djchoices import ChoiceItem, DjangoChoices
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin
from djchoices import DjangoChoices, ChoiceItem
from user.models import User
from categories.models import Team, Category


class Choices(DjangoChoices):
    google = ChoiceItem("GG")
    facebook = ChoiceItem("FB")
    twitter = ChoiceItem("TW")


class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Article(models.Model, HitCountMixin):
    headline = models.CharField(max_length=150)
    photo = models.URLField(max_length=150, null=True)
    video = models.URLField(max_length=150, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField()
    source = models.CharField(max_length=2, choices=Choices.choices)
    content = models.TextField(blank=False)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.headline

    @staticmethod
    def create(headline, author,  content, photo=None, video=None,  source=None, team=None, category=None):
        article = Article(headline=headline, photo=photo, video=video, author=author,
                          source=source, content=content, team=team,
                          category=category)
        article.save()
        return article

    def update(self, headline=None, author=None,  content=None, photo=None, video=None,  source=None, team=None, category=None):
        if headline:
            self.headline = headline
        if author:
            self.author = author
        if content:
            self.content = content
        if photo:
            self.photo = photo
        if video:
            self.video = video
        if source:
            self.source = source
        if team:
            self.team = team
        if category:
            self.category = category

        self.save()
