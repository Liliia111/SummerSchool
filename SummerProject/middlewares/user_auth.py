# pylint: disable=R0205,R1710,R0201,W0613

"""Custom middleware"""
from django.http.response import HttpResponseBadRequest


class AuthenticatedUserMiddleware:
    """Middleware to verify that the user is authenticated"""
    URLS = [
        '/api/v1/user/self/',
        '/api/v1/articles/<int:article_id>/comment/'
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        """Method to verify that the user is authenticated"""
        if not request.user.is_authenticated and request.path in self.URLS:
            return HttpResponseBadRequest()
