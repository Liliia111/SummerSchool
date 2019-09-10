""" Urls for articles """
from django.conf.urls import url
from django.urls import path
from .views import comments_view, ArticleCountHitDetailView, MostPopularView, most_commented

urlpatterns = [
    path('<int:article_id>/comments/', comments_view),
    url(r'^(?P<pk>\d+)/$', ArticleCountHitDetailView.as_view(), name='article_count'),
    path('most_popular/', MostPopularView.as_view(), name='most_popular'),
    path('most_commented/', most_commented),
]
