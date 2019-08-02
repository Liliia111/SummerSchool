from django.shortcuts import render
from django_handlers import Handler
from django.http import HttpResponse

# Create your views here.

handler = Handler()


def index(request):
    return HttpResponse("Hello world!")

