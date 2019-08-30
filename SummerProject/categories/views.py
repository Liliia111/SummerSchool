import operator
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Team


@csrf_exempt
def get_categories(request):
    if request.method == 'GET':

        parent_categs = Category.objects.filter(parent_category_id=None)

        categories_list = []

        for parent_categ in parent_categs:

            child_categs = Category.objects.select_related('parent_category_id').filter(
                parent_category_id=parent_categ.id)
            child_categs_list = []

            for child_categ in child_categs:

                child_subcategs = Team.objects.select_related('category').filter(category=child_categ.id)
                child_subcategs_list = []

                for child_subcateg in child_subcategs:
                    subcateg_dict = {'id': child_subcateg.id, 'name': child_subcateg.name}
                    child_subcategs_list.append(subcateg_dict)

                child_subcategs_list = sorted(child_subcategs_list, key=operator.itemgetter('id'))
                child_categ_dict = {'id': child_categ.id, 'name': child_categ.name,
                                    'subcategories': child_subcategs_list}
                child_categs_list.append(child_categ_dict)

            child_categs_list = sorted(child_categs_list, key=operator.itemgetter('id'))
            categ_dict = {'id': parent_categ.id, 'name': parent_categ.name, 'categories': child_categs_list}
            categories_list.append(categ_dict)

        categories_list = sorted(categories_list, key=operator.itemgetter('id'))

        return JsonResponse(categories_list, safe=False)

    else:

        return HttpResponseBadRequest('Invalid request')
