# pylint: disable=C0111,E1101,R0201
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.views import View
from django.utils.decorators import method_decorator
from .models import User, Role
from .validator import is_user_data_valid_for_create, is_data_valid_for_login
import json


class UserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserView, self).dispatch(request, *args, **kwargs)

    def put(self, request):
        changes = json.loads(request.body.decode('utf-8'))

        first_name = changes['first_name']
        last_name = changes['last_name']

        request.user.update(
            first_name=first_name,
            last_name=last_name,
        )
        return HttpResponse(status=200)


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if not is_user_data_valid_for_create(data):
            return HttpResponseBadRequest()
        user_role = Role.objects.get(pk=1)
        user = User.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password'],
            role=user_role
        )
        return HttpResponse("Success,{} your account created!".format(user.first_name), status=201)
    return HttpResponseBadRequest()


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        if not is_data_valid_for_login(data):
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
