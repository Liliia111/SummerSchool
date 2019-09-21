from django.contrib.auth.backends import ModelBackend
from .models import User


class MyLoginBackend(ModelBackend):
    """Return User record if username + (some test) is valid.
       Return None if no match.
    """

    def authenticate(self, email=None, password=None, request=None):
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None
