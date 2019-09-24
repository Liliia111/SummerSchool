# pylint: disable=C0111,E1101,R0201
import json
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth, get_user_model
from django.contrib.auth.hashers import check_password
from django.views import View
from config.settings import DEFAULT_FROM_EMAIL, HOST
from .models import User
from .tasks import send_reset_email_task
from .validator import is_user_data_valid_for_create, is_data_valid_for_login, is_valid_email_address, \
    is_valid_password_for_reset, is_valid_data_for_update


class UserView(View):
    def put(self, request):
        changes = json.loads(request.body.decode('utf-8'))

        first_name = changes['first_name']
        last_name = changes['last_name']
        email = changes['email']

        if is_valid_data_for_update(changes):

            if User.objects.filter(email=changes['email']).exists():
                return HttpResponseBadRequest()

            request.user.update(
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            return HttpResponse(status=200)

        else:
            return HttpResponseBadRequest()

    def get(self, request):
        logged_user = request.user
        data = {
            'first_name': logged_user.first_name,
            'last_name': logged_user.last_name,
            'email': logged_user.email,
        }
        return JsonResponse(data, safe=False)


def change_password(request):
    if request.method == 'PUT':
        changes = json.loads(request.body.decode('utf-8'))

        old_password = changes['old_password']
        new_password = changes['new_password']

        if check_password(old_password, request.user.password):
            request.user.update(
                password=new_password
            )
            return HttpResponse(status=200)

        return HttpResponseBadRequest()

    return HttpResponseBadRequest()


def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if not is_user_data_valid_for_create(data):
            return HttpResponseBadRequest()
        if User.objects.filter(email=data['email']).exists():
            return HttpResponseBadRequest()
        User.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password'],
        )
        response = HttpResponse(status=201)
        return response

    return HttpResponseBadRequest()


def facebook_registration(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = User.objects.get(email=data['userId'])
        if user:
            auth_login(request, user)
            return HttpResponse(status=100)
        else:
            User.create_user_via_facebook(
                first_name=data['first_name'],
                last_name=data['last_name'],
                userId=data['userId'],
            )
            response = HttpResponse(status=201)
            return response

    return HttpResponseBadRequest()


def login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        if not is_data_valid_for_login(data):
            return HttpResponseBadRequest()
        user = auth(email=data["email"], password=data["password"])
        if user:
            auth_login(request, user)
            response = HttpResponse(status=200, content_type='application/json')
            return response
        return HttpResponseBadRequest()
    return HttpResponseBadRequest()


def logout(request):
    if request.method == "GET":
        auth_logout(request)
        response = HttpResponse(status=200)
        return response
    return HttpResponseBadRequest()


@csrf_exempt
def forgot_password_email_send(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        if not is_valid_email_address(data):
            return HttpResponseBadRequest()
        associated_users = User.objects.filter(email=data['email'])
        if associated_users.exists():
            for user in associated_users:
                content = {
                    'email': user.email,
                    'domain': HOST,
                    'site_name': 'Sport News',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                subject_template_name = 'emails/password_reset_subject.txt'

                email_template_name = 'emails/reset_password.html'

                subject = render_to_string(subject_template_name, content)

                subject = ''.join(subject.splitlines())
                email = render_to_string(email_template_name, content)
                send_reset_email_task.delay(subject, email, user.email)

            return HttpResponse(status=200)

        return HttpResponseBadRequest()

    return HttpResponseBadRequest()


@csrf_exempt
def forgot_password_reset_confirm(request, uidb64=None, token=None):
    if request.method == "GET":
        UserModel = get_user_model()
        assert uidb64 is not None and token is not None
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel.objects.get(pk=uid)
            request.session['uid'] = uid.decode("utf-8")
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            return redirect('/resetPassword')

    return HttpResponseBadRequest()


@csrf_exempt
def forgot_password_handler(request):
    if request.method == "POST":
        UserModel = get_user_model()
        user = UserModel.objects.get(pk=int(request.session.get('uid')))
        data = json.loads(request.body.decode('utf-8'))
        if user is not None:
            if is_valid_password_for_reset(data):
                new_password = data['new_password_confirm']
                user.set_password(new_password)
                user.save()
                return HttpResponse(status=201)

    return HttpResponseBadRequest()


