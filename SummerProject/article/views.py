from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from .models import Article
from django.db import transaction
import json
from .forms import CommentForm


""" View for comment backend"""
@transaction.atomic
def comment_form(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        data = request.body.decode('utf8')
        data = json.loads(data)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment.content = data["content"]
            comment.user = request.user
            comment.save()
            article.comments.add(comment)
            response = HttpResponse(status=201)
            response['comment_id'] = comment.id
            return response
    else:
        return HttpResponseBadRequest


""" View for getting existing comments"""
@transaction.atomic
def viewing_comments(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "GET":
        data = list(article.comments.all().values())
        return JsonResponse(data, safe=False)
    else:
        return HttpResponseBadRequest
