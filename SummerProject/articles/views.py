from django.utils import timezone
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views import View
from articles.models import Article
from user.models import User
from categories.models import Category
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.db import transaction
import json
from django.db.models import Count
from .forms import CommentForm
from datetime import datetime


class ArticleDetailView(View):

    def get_queryset(self):
        return Article.objects.all()

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        categories = get_object_or_404(Category, pk=pk)
        res = model_to_dict(article)
        cat_res = model_to_dict(categories)
        user = User.objects.get(pk=res['author'])
        res['author'] = user.first_name + " " + user.last_name
        formatedDate = res['published_date'].strftime("%d.%m.%Y")
        res['published_date'] = formatedDate
        res['category'] = cat_res['name']
        return JsonResponse(res)


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


@transaction.atomic
def most_commented(request):
    if request.method == "GET":
        data = list(Article.objects.values().annotate(art_comments=Count('comments')).order_by('-art_comments')[:3])
        return JsonResponse(data, safe=False)


@transaction.atomic
def more_articles(request):
    if request.method == "GET":
        result = list(Article.objects.values().annotate(articles=Count('id')).order_by('-articles')[1:4])
        categ = list(Category.objects.values())
        for i in range(0, len(result)):
            result[i]['category_id'] = categ[i]['name']
        return JsonResponse(result, safe=False)

@transaction.atomic
def more_articles_2(request):
    if request.method == "GET":
        result = list(Article.objects.values().annotate(articles=Count('id')).order_by('-articles')[4:7])
        categ = list(Category.objects.values())
        for i in range(0, len(result)):
            result[i]['category_id'] = categ[i]['name']
        return JsonResponse(result, safe=False)