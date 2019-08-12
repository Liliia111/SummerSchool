from django.core.validators import validate_email


class Validator:
    @staticmethod
    def valid_data_for_creating_user(data):
        params = ["first_name", "last_name", "email", "password"]
        for k in data.keys():
            if k not in params:
                print(k)
                return False
        if len(data["first_name"]) > 70 or len(data["last_name"]) > 50 or len(data["password"]) > 10000:
            return False
        # TODO: check for unique and is email correct
        # if not validate_email(data["email"]):
        #     return False
        return True

    @staticmethod
    def valid_data_for_login(data):
        params = ["email", "password"]
        for k in data.keys():
            if k not in params:
                return False
        # if not validate_email(data["email"]):
        #     return False
        return True