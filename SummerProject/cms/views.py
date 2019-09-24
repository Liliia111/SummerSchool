from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.shortcuts import get_object_or_404
import json
from articles.models import Article, Comment


class ArticleView(View):
    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        article = Article.create(headline=data["headline"], photo=data["photo"], video=data["video"], author=request.user,
                          source=data["source"], content=data["content"])
        response = HttpResponse(status=201)
        response['article_id'] = article.id
        return response

    def put(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        article = Article.update(headline=data["headline"], photo=data["photo"], video=data["video"], author=request.user,
                          source=data["source"], content=data["content"])
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
        except Comment.DoesNotExist:
            return HttpResponseBadRequest()


class CommentView(View):
    def delete(self, request):
        data = json.loads(request.body.decode('utf-8'))

        article_id = data["article_id"]
        comment_id = data["comment_id"]

        article = get_object_or_404(Article, pk=article_id)
        try:
            article.comments.get(id=comment_id).delete()
            return HttpResponse(status=204)
        except Comment.DoesNotExist:
            return HttpResponseBadRequest()