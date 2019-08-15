from django.core.management.base import BaseCommand
from articles.models import Article
from django.forms.models import model_to_dict
import csv
import logging


class Command(BaseCommand):
    help = "Shows multiple articles staring from specified"
    logger = logging.getLogger(__name__)

    @staticmethod
    def get_content(queryset):
        rows_list = list()
        for article in queryset:
            dict_article = model_to_dict(article)
            article_content = [dict_article["id"], dict_article["title"], dict_article["content"]]
            rows_list.append(article_content)

        Command.logger.info("Amount of received articles {}".format(len(rows_list)))
        return rows_list

    def add_arguments(self, parser):
        parser.add_argument('-am', '--articles_amount', type=int, help='Determines the number of returned articles')
        parser.add_argument('-pk', type=int, help='Determines starting pk value')

    def handle(self, *args, **kwargs):

        am = kwargs['articles_amount']
        pk = kwargs['pk']

        self.logger.info("-am parameter {}, -pk parameter {}".format(am, pk))
        # context manager
        with open("articles/articles.csv", "w") as articles:
            self.logger.info("articles.csv file was successfully created")
            writer = csv.writer(articles)
            articles_pk_list = Article.objects.all().order_by('id')[pk:pk+am]

            for article in self.get_content(articles_pk_list):
                writer.writerow(article)

