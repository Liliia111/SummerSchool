from django.contrib.auth.views import redirect_to_login
from django.utils.deprecation import MiddlewareMixin
from django.http.response import HttpResponseBadRequest


class GetCustomUser(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated and request.path == '/api/v1/auth/update_info/':
            return HttpResponseBadRequest()
