from django.http import HttpResponse
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.


def index(request):

    return HttpResponse("Hello world!")


class ListArticleView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_auth(self, serializer):
        serializer.save()


class ArticleDetail(generics.RetrieveAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
