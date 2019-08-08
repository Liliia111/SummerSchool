import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Article


def index():
    return HttpResponse("Hello, world. You're at the blog index.")


class ArticleList(View):
    def get(self, request):
        article_list = list(Article.objects.values())
        page = request.GET.get('page', 1)
        paginator = Paginator(article_list, 10)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        return JsonResponse(articles.object_list, safe=False)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleList, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)

        try:
            new_article = Article(title=data["title"], content=data["content"])
            new_article.full_clean()
            new_article.save()
            return JsonResponse(status=201, data=data, safe=False)
        except:
            message = "not valid data"
            return JsonResponse(status=400, data={'error': message})


class ArticleDetail(View):

    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            article_object = {'title': article.title, 'content': article.content}
            return JsonResponse(article_object, safe=False)
        except Article.DoesNotExist:
            message = "primary key does not exist"
            return JsonResponse(status=404, data={'error': message})

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
            new_article.full_clean()
            new_article.save()
            new_article.save()
            return JsonResponse(status=201, data=data, safe=False)
        except Article.DoesNotExist:
            message = "primary key does not exist"
            return JsonResponse(status=404, data={'error': message})
        except:
            message = "not valid data"
            return JsonResponse(status=400, data={'error': message})

    def delete(self, request, pk):
        try:
            new_article = Article.objects.get(pk=pk)
            new_article.delete()
            return HttpResponse(status=204)
        except Article.DoesNotExist:
            message = "primary key does not exist"
            return JsonResponse(status=404, data={'error': message})
