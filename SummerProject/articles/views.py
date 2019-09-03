from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.views import View
from articles.models import Article
from django.forms.models import model_to_dict

class ArticleDetailView(View):
    def get_queryset(self):
        return Article.objects.all()
    def get(self, request, pk):
        try:
            article = model_to_dict(Article.objects.get(pk=pk), fields=['id', 'headline', 'photo', 'video', 'author', 'source', 'content', 'team', 'category', 'comments'])
            response = JsonResponse(article, safe=False)
            response['custom_id'] = pk
            return response
        except Article.DoesNotExist:
            message = "primary key does not exist"
            return JsonResponse(status=404, data={'error': message})
