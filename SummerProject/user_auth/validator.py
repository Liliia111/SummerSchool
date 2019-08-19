from django.core.validators import validate_email
from django.core.validators import ValidationError

first_name_len = 50
last_name_len = 50
password_len = 100


def valid_data_for_creating_user(data):
    params = ["first_name", "last_name", "email", "password"]
    for k in data.keys():
        if k not in params:
            print(k)
            return False
    if len(data["first_name"]) > first_name_len or len(data["last_name"]) > last_name_len or len(
            data["password"]) > password_len:
        return False
    try:
        validate_email(data["email"])
    except ValidationError:
        return False
    return True


def valid_data_for_login(data):
    params = ["email", "password"]
    for k in data.keys():
        if k not in params:
            return False
    try:
        validate_email(data["email"])
    except ValidationError:
        return False
    return True
