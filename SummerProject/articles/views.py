from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Article
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import model_to_dict

ARTICLES_NUMBER_PER_PAGE = 3


class ArticleView(View):

    def get(self, request):
        articles_list = list(Article.objects.values('id', 'title', 'content').all())
        paginator = Paginator(articles_list, ARTICLES_NUMBER_PER_PAGE)
        page = request.GET.get('page', 1)

        try:
            article_list = paginator.page(page)
        except PageNotAnInteger:
            article_list = paginator.page(1)
        except EmptyPage:
            article_list = paginator.page(paginator.num_pages)

        response = HttpResponse(article_list)
        response['custom'] = 'custom get articles'
        return response

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        articles = Article(title=data["title"], content=data["content"])
        articles.save()
        if len(data["title"]) > 300:
            return HttpResponse(status=400)
        else:
            response = JsonResponse(data, safe=False, status=201)
            return response


class ArticleDetailView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleDetailView, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        article = model_to_dict(Article.objects.get(pk=pk), fields=['title', 'content'])
        response = JsonResponse(article, safe=False)
        response['custom_id'] = pk
        return response

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
            response = JsonResponse({"updated": data}, safe=False, status=200)
            response['custom_id'] = pk
            return response
        except Article.DoesNotExist:
            response = JsonResponse({"error": "pk doesn't exist"}, safe=False, status=404)
            return response
        except:
            return JsonResponse({"error": "not valid data"}, safe=False)

    def delete(self, request, pk):
        try:
            new_article = Article.objects.get(pk=pk)
            new_article.delete()
            response = JsonResponse({"deleted": True}, safe=False, status=204)
            return response
        except:
            return JsonResponse({"error": "not valid pk"}, safe=False)