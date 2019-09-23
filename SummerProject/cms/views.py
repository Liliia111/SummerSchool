from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
import json
from articles.models import Article,  Comment

# Create your views here.
class CmsArticleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CmsArticleView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        # here must be validation method
        data = request.body.decode('utf8')
        data = json.loads(data)
        article = Article(headline=data["headline"], photo=data["photo"], video=data["video"], author=request.user,
                          source=data["source"], content=data["content"], team=data["team"],
                          category=data["category"])
        article.save()
        response = HttpResponse(status=201)
        response['article_id'] = article.id
        return response


# Create your views here.

class CommentView(View):
    def delete(self, request):
        data = json.loads(request.body.decode('utf-8'))

        article_id = data["article_id"]
        comment_id = data["comment_id"]

        article = get_object_or_404(Article, pk=article_id)
        try:
            article.comments.get(id=comment_id).delete()
            return HttpResponse(status=200)
        except Comment.DoesNotExist:
            return HttpResponseBadRequest()
