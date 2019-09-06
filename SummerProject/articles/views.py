from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.views import View
from articles.models import Article
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404


class ArticleDetailView(View):

    def get_queryset(self):
        return Article.objects.all()

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        return JsonResponse(model_to_dict(article))
