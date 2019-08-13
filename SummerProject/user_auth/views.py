from django.http import HttpResponse, HttpResponseBadRequest
from .models import User
from .validator import valid_data_for_login, valid_data_for_creating_user
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.views import View
from django.utils.decorators import method_decorator


class UserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserView, self).dispatch(request, *args, **kwargs)

    def put(self, request):
        changes = json.loads(request.body.decode('utf-8'))

        if 'id' in request.session:
            user_id = request.session['id']
        else:
            return HttpResponseBadRequest()

        user = User.objects.get(id=user_id)
        print(user.first_name)
        if not user:
            return HttpResponseBadRequest()

        first_name = changes['first_name']
        last_name = changes['last_name']

        user.update(
            first_name=first_name,
            last_name=last_name,
        )
        print(user.first_name)
        return HttpResponse(status=200)


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
