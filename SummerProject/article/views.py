from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from .models import Article
from django.db import transaction
import json
from .forms import CommentForm
from django.views.decorators.csrf import csrf_exempt


""" View for comment backend"""
@csrf_exempt
@transaction.atomic
def comments_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "GET":
        data = list(article.comments.all().values())
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = request.body.decode('utf8')
        data = json.loads(data)
        form = CommentForm(data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            article.comments.add(comment)
            response = HttpResponse(status=201)
            response['comment_id'] = comment.id
            response['article_id'] = article_id
            return response
    else:
        return HttpResponseBadRequest
