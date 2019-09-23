from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.forms import model_to_dict
from django.views import View
from hitcount.views import HitCountDetailView
from django.shortcuts import get_object_or_404
from django.db import transaction
import json
from django.db.models import Count
from articles.models import Article
from django.views.decorators.csrf import csrf_exempt
from .models import Article, Comment
from user.models import User


MOST_POPULAR_COUNT = 3


class ArticleDetailView(View):

    def get_queryset(self):
        return Article.objects.all()

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        return JsonResponse(model_to_dict(article))


""" View for comment backend"""


def user_data_adding(comments_data, user_ids):
    for i in range(len(user_ids)):
        user = get_object_or_404(User, id=user_ids[i]['user_id'])
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        comments_data[i].update(user_data)

    return comments_data


""" View for comment backend"""


@csrf_exempt
@transaction.atomic
def comments_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "GET":
        comments_data = list(article.comments.all().values('id', 'content', 'date'))
        user_ids = list(article.comments.values('user_id'))
        data = user_data_adding(comments_data, user_ids)
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = request.body.decode('utf8')
        data = json.loads(data)
        comment = Comment(content=data["comment"], user=request.user)
        comment.save()
        article.comments.add(comment)
        print("Comments was saved and added")
        response = HttpResponse(status=201)
        response['comment_id'] = comment.id
        response['article_id'] = article_id
        return response
    else:
        return HttpResponseBadRequest


""" View for most popular articles"""


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


""" View for most commented articles"""


@transaction.atomic
def most_commented(request):
    if request.method == "GET":
        data = list(Article.objects.values().annotate(art_comments=Count('comments')).order_by('-art_comments')[:3])
        return JsonResponse(data, safe=False)
