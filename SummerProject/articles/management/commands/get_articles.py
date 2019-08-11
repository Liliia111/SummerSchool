from django.core.management.base import BaseCommand
from articles.models import Article
from django.forms.models import model_to_dict
import csv
import bisect


class Command(BaseCommand):
    help = "Shows multiple pages staring from specified"

    def add_arguments(self, parser):
        parser.add_argument('articles_amount', type=int, help='Determines the number of returned articles')
        parser.add_argument('pk', type=int, help='Determines starting pk value')

    def handle(self, *args, **kwargs):
        am = kwargs['articles_amount']
        pk = kwargs['pk']

        with open("articles/articles.csv", "w") as articles:
            writer = csv.writer(articles)
            # writer.writerow(['id', 'title', 'content'])
            articles_list = list(Article.objects.values('id').all())
            articles_pk_list = []

            for i in articles_list:
                articles_pk_list.append(i['id'])

            for i in range(am):
                try:
                    article = Article.objects.get(pk=pk)
                    dict_article = model_to_dict(article)
                    row = [dict_article["id"], dict_article["title"], dict_article["content"]]
                    writer.writerow(row)
                except article.DoesNotExist:
                    index = bisect.bisect_right(articles_pk_list, pk)
                    try:
                        pk = articles_pk_list[index]
                    except IndexError:
                        break
                    article = Article.objects.get(pk= pk)
                    dict_article = model_to_dict(article)
                    row = [dict_article["id"], dict_article["title"], dict_article["content"]]
                    writer.writerow(row)

                pk += 1
        articles.close()

        return "Success! Check articles.csv file for content!"
