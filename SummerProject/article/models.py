from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin
from django.utils.encoding import python_2_unicode_compatible
from user.models import User
from categories.models import Team, Category, SocialNetworkChoice


class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


@python_2_unicode_compatible
class Article(models.Model, HitCountMixin):
    headline = models.CharField(max_length=150)
    photo = models.URLField(max_length=150, null=True)
    video = models.URLField(max_length=150, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=8, choices=[(tag, tag.value) for tag in SocialNetworkChoice])
    content = models.TextField(blank=False)
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')
