
from rest_framework import serializers
from .models import Article


class ArticlesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Article
        fields = ['id', 'title', 'content']
        read_only_fields = ('title', 'content')