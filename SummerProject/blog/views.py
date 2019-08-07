from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
import json
from blog.models import Article
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


class ArticleList(View):
    def get(self, request):
        article_list = list(Article.objects.values())
        return JsonResponse(article_list, safe=False)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleList, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            new_article = Article(title=data["title"], content=data["content"])
            new_article.save()
            return JsonResponse(data, safe=False)
        except:
            return JsonResponse({"error": "not valid data"}, safe=False)


class ArticleDetail(View):

    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        article_list = {'title': article.title, 'content': article.content}
        return JsonResponse(article_list, safe=False)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleDetail, self).dispatch(request, *args, **kwargs)

    def put(self, request, pk):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            new_article = Article.objects.get(pk=pk)
            data_key = list(data.keys())
            for key in data_key:
                if key == "title":
                    new_article.title = data[key]
                if key == "content":
                    new_article.content = data[key]
            new_article.save()
            return JsonResponse(data, safe=False)
        except Article.DoesNotExist:
            return JsonResponse({"error": "primary key does not exist"}, safe=False)
        except:
            return JsonResponse({"error": "not valid data"}, safe=False)

    def delete(self, request, pk):
        try:
            new_article = Article.objects.get(pk=pk)
            new_article.delete()
            return JsonResponse({"deleted": True}, safe=False)
        except:
            return JsonResponse({"error": "not valid primary key"}, safe=False)
# class ArticleList(APIView):
#
#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ArticleDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ArticleSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
