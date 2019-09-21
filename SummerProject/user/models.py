from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager


class Role(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    @staticmethod
    def create(first_name, last_name, email, password):
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        return user

    @staticmethod
    def create_user_via_facebook(first_name, last_name, userId):
        user = User(first_name=first_name, last_name=last_name, email=userId)
        user.set_unusable_password()
        user.save()
        return user

    def update(self, first_name=None, last_name=None, password=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if password:
            self.set_password(password)

        self.save()
