from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from .models import Article
from django.db import transaction

from .forms import CommentForm


""" View for comment backend"""
@transaction.atomic
def comment_form(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            article.comments.add(comment)
            response = HttpResponse(status=201)
            response['comment_id'] = comment.id
            return response
    else:
        return HttpResponseBadRequest
