from django.shortcuts import render
from django_handlers import Handler
from django.http import HttpResponse, JsonResponse
# Create your views here.
handler = Handler()
@handler.get('index')
def index(request):
    return render(request, "index.html")

@handler.get('random_string')
def text(request):
    return HttpResponse("WE ARE GOING TO BE ...")

@handler.get('json_bitch')
def json_data(request):
    data = {
        'Soft': 'Serve',
        'Porn': 'Hub',
        'Pasha': 'TexHiK',
    }
    return JsonResponse(data)
