from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=2000)

    def create(self, data):
        return Article.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.content = data.get('content', instance.content)
        instance.save()
        return instance
