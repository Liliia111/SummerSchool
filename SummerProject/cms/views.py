from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.shortcuts import get_object_or_404
import json
from articles.models import Article, Comment


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
