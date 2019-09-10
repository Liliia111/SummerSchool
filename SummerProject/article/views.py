from django.forms import model_to_dict
from django.views import View
from hitcount.views import HitCountDetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from .models import Article
from django.db import transaction
import json
from .forms import CommentForm

""" View for comment backend"""
MOST_POPULAR_COUNT = 3


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


class ArticleCountHitDetailView(HitCountDetailView):
    model = Article
    count_hit = True  # set to True if you want it to try and count the hit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MostPopularView(View):
    def get(self, request):
        articles = Article.objects.order_by("-hit_count_generic__hits")[:MOST_POPULAR_COUNT]
        popular_list = [model_to_dict(article) for article in articles]
        return JsonResponse(popular_list, safe=False)
