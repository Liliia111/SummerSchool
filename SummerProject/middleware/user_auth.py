# pylint: disable=R0205,R1710,R0201

"""Custom middleware"""
from django.http.response import HttpResponseBadRequest


class AuthenticatedUser(object):
    """Middleware to verify that the user is authenticated"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        """Method to verify that the user is authenticated"""
        if not request.user.is_authenticated and request.path == '/api/v1/user/update_info/':
            return HttpResponseBadRequest()
