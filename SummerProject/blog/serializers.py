
from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    content = serializers.CharField(max_length=300)

    def create(self, data):
        return Article.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.content = data.get('content', instance.content)
        instance.save()
        return instance
