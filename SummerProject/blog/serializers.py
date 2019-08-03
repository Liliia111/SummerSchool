from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import Group, Permission


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "content")
