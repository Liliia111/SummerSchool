from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def json_test(request):
    responseDataJSON = {
    'text': 'this is JSON response',
    }
    return JsonResponse(responseDataJSON)


def txt_test(request):
    some_txt = "txt_Test file"
    return HttpResponse(some_txt)
