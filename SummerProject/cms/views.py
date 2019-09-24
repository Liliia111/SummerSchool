from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
import json
from articles.models import Article
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404


# Create your views here.
class CmsArticleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CmsArticleView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        # here must be validation method
        data = request.body.decode('utf8')
        data = json.loads(data)
        article = Article.create(headline=data["headline"], photo=data["photo"], video=data["video"], author=request.user,
                          source=data["source"], content=data["content"], team=data["team"],
                          category=data["category"])
        response = HttpResponse(status=201)
        response['article_id'] = article.id
        return response

    def put(self, request):
        # here must be validation method
        data = request.body.decode('utf8')
        data = json.loads(data)
        article = Article.update(headline=data["headline"], photo=data["photo"], video=data["video"], author=request.user,
                          source=data["source"], content=data["content"], team=data["team"],
                          category=data["category"])
        response = HttpResponse(status=202)
        response['article_id'] = article.id
        return response

    def delete(self, request):
        data = json.loads(request.body.decode('utf-8'))

        article_id = data["article_id"]

        article = get_object_or_404(Article, pk=article_id)
        try:
            article.get(id=article_id).delete()
            return HttpResponse(status=204)
        except Article.DoesNotExist:
            return HttpResponseBadRequest()
