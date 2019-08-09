from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ArticlePagePaginator(object):
    min_limit = 1
    max_limit = 10
    def paginate(self, articles_list, page=1, limit=10, **kwargs):
        try:
            if page is None:
                page = 1
            if page < 1:
                page = 1
            page = int(page)
        except (TypeError, ValueError):
            page = 1

        try:
            limit = int(limit)
            if limit < self.min_limit:
                limit = self.min_limit
            if limit > self.max_limit:
                limit = self.max_limit
        except (ValueError, TypeError):
            limit = self.max_limit

        paginator = Paginator(articles_list, limit)
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        data = {
            'previous_page': objects.has_previous() and objects.previous_page_number() or None,
            'next_page': objects.has_next() and objects.next_page_number() or None,
            'data': list(objects)
        }
        return data
