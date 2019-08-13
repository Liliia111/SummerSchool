from django.http import HttpResponse, HttpResponseBadRequest
from .models import User
from .validator import valid_data_for_login, valid_data_for_creating_user
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if not valid_data_for_creating_user(data):
            return HttpResponseBadRequest()
        user = User.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password']
        )
        return HttpResponse("Success,{} your account created!".format(user.first_name), status=201)
    return HttpResponseBadRequest()


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        if not valid_data_for_login(data):
            return HttpResponseBadRequest()
        user = authenticate(email=data["email"], password=data["password"])
        if user:
            auth_login(request, user)
            response = HttpResponse(status=200)
            request.session['id'] = user.id
            return response
        return HttpResponseBadRequest()
    return HttpResponseBadRequest()


@csrf_exempt
def logout(request):
    if request.method == "GET":
        auth_logout(request)
        response = HttpResponse(status=200)
        if 'id' in request.session:
            del request.session['id']
        return response
    return HttpResponseBadRequest
