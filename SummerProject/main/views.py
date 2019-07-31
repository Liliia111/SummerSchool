from django.shortcuts import render
from django_handlers import Handler
from django.http import JsonResponse, HttpResponse

handler = Handler()

# Create your views here.
def index(request):
    return render(request, "index.html")

@handler.get('jsn_endpoint')
def jsn_endpoint(request):
    data = {

        'just': 'some data'
    }
    return JsonResponse(data)

@handler.get('html_endpoint')
def html_endpoint(request):
    return render(request, "index.html")

@handler.get('txt_endpoint')
def txt_endpoint(request):
    return HttpResponse("Hello, World")
