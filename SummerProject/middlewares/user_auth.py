# pylint: disable=R0205,R1710,R0201,W0613

"""Custom middleware"""
from django.http.response import HttpResponseBadRequest


class AuthenticatedUserMiddleware:
    """Middleware to verify that the user is authenticated"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        """Method to verify that the user is authenticated"""
        if not request.user.is_authenticated and request.path == '/api/v1/user/self/':
            return HttpResponseBadRequest()
