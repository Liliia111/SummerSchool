from django.shortcuts import render
# from django_handlers import Handler
from .models import Article
from rest_framework import generics
from .serializers import ArticlesSerializer

# Create your views here.
# handler_general = Handler()
#
#
# @handler_general.get('articles')
# def view_articles(request):
#     # here we should show all the our articles titles/ look on computer
#     # articles = Article.objects.all()
#     # return render(request, 'general.html', {'articles': [article.data for article in articles]})
#     return Http


class CreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

    def perform_create(self, serializer):
        serializer.save()
