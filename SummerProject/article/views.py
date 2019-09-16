from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from .models import Article
from user.models import User
from django.db import transaction
import json
from .forms import CommentForm
from django.views.decorators.csrf import csrf_exempt

""" Function for adding user data to each dict """


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
        form = CommentForm(data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            print("Comment was saved")
            article.comments.add(comment)
            print("Comment was added to article")
            response = HttpResponse(status=201)
            response['comment_id'] = comment.id
            response['article_id'] = article_id
            return response
    else:
        print("Form is incorrect")
        return HttpResponseBadRequest
