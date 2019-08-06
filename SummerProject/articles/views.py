# from django.shortcuts import render
# from django_handlers import Handler
# from rest_framework import generics
# from django.http import HttpResponse, JsonResponse
from .models import Article
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticlesSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


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

#
# class CreateView(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#
# class DetailsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer

@api_view(['GET', 'POST'])
@csrf_exempt
def article_list(request, format=None):
    """View for getting all articles and post new one"""
    if request.method == 'GET':
        articles = Article.objects.values('title', 'content').all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticlesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def article_details(request, pk, format=None):
    """View for get, put and delete article with certain pk"""

    try:
        article = Article.objects.values('title', 'content').get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticlesSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticlesSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)