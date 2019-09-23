from django.conf.urls import url
from django.urls import path
from .views import ArticleDetailView, comments_view, most_commented, MostPopularView, \
    ArticleCountHitDetailView

urlpatterns = [
    path('<int:pk>/detail/', ArticleDetailView.as_view()),
    path('<int:article_id>/comments/', comments_view),
    path('most_commented/', most_commented),
    url(r'^(?P<pk>\d+)/$', ArticleCountHitDetailView.as_view(), name='article_count'),
    path('most_popular/', MostPopularView.as_view(), name='most_popular'),
    path('most_commented/', most_commented),
]