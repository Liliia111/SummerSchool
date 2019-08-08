from django.http import JsonResponse
from django.views import View
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


class ArticleView(View):
    def get(self, request):
        friend_list = list(Article.objects.values())
        return JsonResponse(friend_list, safe=False)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        articles = Article(title=data["title"], content=data["content"])
        articles.save()
        return JsonResponse({"created": data}, safe=False)


class ArticleDetailView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleDetailView, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        article_list = {"article": list(Article.objects.filter(pk=pk).values())}
        return JsonResponse(article_list, safe=False)

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
            return JsonResponse({"updated": data}, safe=False)
        except Article.DoesNotExist:
            return JsonResponse({"error": "Your friend having provided primary key does not exist"}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)

    def delete(self, request, pk):
        try:
            new_article = Article.objects.get(pk=pk)
            new_article.delete()
            return JsonResponse({"deleted": True}, safe=False)
        except:
            return JsonResponse({"error": "not a valid primary key"}, safe=False)