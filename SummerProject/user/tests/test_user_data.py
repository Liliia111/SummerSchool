import pytest
from user.models import User
import random
import string


'''Registration and Login'''
@pytest.fixture()
def create_user(db, client):
    def inner():
        email = "{}@mail.com".format(''.join([random.choice(string.ascii_lowercase) for n in range(10)]))
        password = "44456"
        client.post('/api/v1/user/registration/', data={'first_name': 'Max',
                                                        'last_name': 'NewMax',
                                                        'email': email,
                                                        'password': password}, content_type='application/json')
        client.post('/api/v1/user/login/', data={'email': email,
                                                 'password': password}, content_type='application/json')
        user = User.objects.get(email=email)

        return user
    return inner


@pytest.mark.django_db
def test_user_data(client, create_user):
    new_user = create_user()
    response = client.get('/api/v1/user/self/')
    assert response.json() == {
        'first_name': new_user.first_name,
        'last_name': new_user.last_name,
        'email': new_user.email,
    }
    assert response['content-type'] == 'application/json'
    assert response.status_code == 200
