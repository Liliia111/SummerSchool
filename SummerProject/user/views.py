# pylint: disable=C0111,E1101,R0201
import json
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.base import Token
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, get_user_model
from django.views import View
from django.utils.decorators import method_decorator
from config.settings import DEFAULT_FROM_EMAIL
from .models import User
from .validator import is_user_data_valid_for_create, is_data_valid_for_login, is_valid_email_address, \
    is_valid_password_for_reset

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
        if User.objects.filter(email=data['email']).exists():
            return HttpResponseBadRequest()
        user = User.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password'],
        )
        return HttpResponse(status=201)
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
                    'domain': request.META['HTTP_HOST'],
                    'site_name': 'Sport News',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                subject_template_name = 'password_reset_subject.txt'

                email_template_name = 'reset_password.html'

                subject = render_to_string(subject_template_name, content)

                subject = ''.join(subject.splitlines())
                email = render_to_string(email_template_name, content)
                send_mail(subject, email, DEFAULT_FROM_EMAIL, [user.email], html_message=email, fail_silently=False)

            return redirect('/check-email')

        return HttpResponseBadRequest()

    return HttpResponseBadRequest()


@csrf_exempt
def forgot_password_reset_confirm(request, uidb64=None, token=None):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        UserModel = get_user_model()
        assert uidb64 is not None and token is not None
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if is_valid_password_for_reset(data):
                new_password = data['new_password_confirm']
                user.set_password(new_password)
                user.save()
                return HttpResponse(status=201)

    return HttpResponseBadRequest()
