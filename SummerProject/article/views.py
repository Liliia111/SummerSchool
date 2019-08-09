from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from .Paginator import ArticlePagePaginator
from .models import Article

page = 1

class Article_V(ArticlePagePaginator,View):
    def get(self, request):
        articles = Article.objects.values()
        articles_use = list(articles)
        return JsonResponse({"articles_list": self.paginate(articles_use, page=3, limit=3)})

    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Article_V, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        articles = Article(title=data["title"], description=data["description"], body=data["body"])
        articles.save()
        return JsonResponse({"created": data}, safe=False)

class ArticleDetail(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleDetail, self).dispatch(request, *args, **kwargs)

    def get(self, request, id):
        articles = {"article": list(Article.objects.filter(pk=id).values())}
        return JsonResponse(articles, safe=False)

    def put(self, request, id):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            article = Article.objects.get(pk=id)
            data_key = list(data.keys())
            for key in data_key:
                if key == "title":
                    article.title = data[key]
                if key == "description":
                    article.description = data[key]
                if key == "body":
                    article.body = data[key]
            article.save()
            return JsonResponse({"updated": data}, safe=False)
        except Article.DoesNotExist:
            return JsonResponse({"error": "Your friend having provided primary key does not exist"}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)

    def delete(self, request, id):
        try:
            article = Article.objects.get(pk=id)
            article.delete()
            return JsonResponse({"deleted": True}, safe=False, status=204)
        except:
            return JsonResponse({"error": "not a valid primary  key"}, safe=False)