import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def categories(request):
    #json_string = json.dumps(['lalala', 'alala', 'lalala'])
    # return render(request,
    #               'index.html',
    #               {'categories': json.dumps(c)}
    #               )
    # return HttpResponse(json_stuff, content_type="application/json")
    # return HttpResponse("Hello, world. You're at the polls index.")
    # Create your views here.
    return JsonResponse(['NFL', 'NBA', 'MLB', 'NHL', 'CBB','CFB', 'NASCAR', 'GOLF', 'SOCCER', 'MORE', 'LIFESTYLE', 'DEALBOOK', 'VIDEO'], safe=False)
    #return render(request, 'index.html', {'json_string':json_string })


