from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
import json
from articles.models import Article
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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