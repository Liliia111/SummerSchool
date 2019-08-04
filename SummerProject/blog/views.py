from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django_handlers import Handler
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status, APIView
from blog.models import Article
from blog.serializers import ArticleSerializer

handler = Handler()


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


# class ListCreateSongsView(generics.ListCreateAPIView):
#     """
#     GET songs/
#     POST songs/
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def post(self, request, *args, **kwargs):
#         an_article = Article.objects.create(
#             title=request.data["title"],
#             content=request.data["content"]
#         )
#         return Response(
#             data=ArticleSerializer(an_article).data,
#             status=status.HTTP_201_CREATED
#         )
class ArticleList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    """
    Retrieve, update or delete an article instance.
    """

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ArticleSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#
# @handler.get('articles')
# def view_articles(request):
#     articles = Article.objects.all()
#     return JsonResponse({
#         'title': [title.data for title in articles],
#         'content': [content.data for content in articles]
#     })
#


# @handler.post('articles')
# def add_record(request):
#     form = RecordForm(json.loads(request.body))
#
#     if form.is_valid():
#         record = form.save()
#         return JsonResponse(record.data)
#
#     return JsonResponse(form.errors, status=422)
