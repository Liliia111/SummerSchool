from django.core.validators import validate_email
from django.core.validators import ValidationError

FIRST_NAME_MAX_LEN = 50
LAST_NAME_MAX_LEN = 50
PASSWORD_MAX_LEN = 255
PASSWORD_MIN_LEN = 4


def is_user_data_valid_for_create(data):
    params = ["first_name", "last_name", "email", "password"]
    for k in data.keys():
        if k not in params:
            return False
        if len(data[k]) == 0:
            return False
    if len(data["first_name"]) > FIRST_NAME_MAX_LEN or len(data["last_name"]) > LAST_NAME_MAX_LEN or len(
            data["password"]) > PASSWORD_MAX_LEN or len(data["password"]) < PASSWORD_MIN_LEN:
        return False
    try:
        validate_email(data["email"])
    except ValidationError:
        return False
    return True


def is_data_valid_for_login(data):
    params = ["email", "password"]
    for k in data.keys():
        if k not in params:
            return False
        if len(data[k]) == 0:
            return False
    try:
        validate_email(data["email"])
    except ValidationError:
        return False
    return True