import pytest
from django.core import mail
from django.urls import reverse
from user.models import User

PASSWORD = "test"


@pytest.fixture()
def user():
    return User.create(first_name="first_name", last_name="last_name", email="test@test.com", password=PASSWORD)


@pytest.mark.django_db
def test_forgot_password_reset(client, user):
    response = client.post(reverse('forgot_password'), {'email': user.email}, content_type='application/json')
    assert response.status_code == 200

    token = response.context[0]['token']
    uid = response.context[0]['uid']
    response = client.get(reverse('password_reset_confirm', kwargs={'token': token, 'uidb64': uid}))

    assert response.status_code == 302

    data = {
        'new_password': PASSWORD + "1",
        'new_password_confirm': PASSWORD + "1"
    }
    response = client.post(reverse('forgot_password_handler'),
                           data=data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.parametrize("new_password, new_password_confirm", [
    (PASSWORD * 3000, PASSWORD * 3000),
    (PASSWORD * 3000, PASSWORD),
    (PASSWORD + '1', PASSWORD),
    ("", ""),
    ("", PASSWORD)
])
@pytest.mark.django_db
def test_invalid_data_password_reset(client, user, new_password, new_password_confirm):
    response = client.post(reverse('forgot_password'), {'email': user.email}, content_type='application/json')
    assert response.status_code == 200

    token = response.context[0]['token']
    uid = response.context[0]['uid']
    response = client.get(reverse('password_reset_confirm', kwargs={'token': token, 'uidb64': uid}))

    assert response.status_code == 302

    data = {
        'new_password': new_password,
        'new_password_confirm': new_password_confirm
    }
    response = client.post(reverse('forgot_password_handler'),
                           data=data, content_type='application/json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_forgot_password_reset_link_after_password_was_changed(client, user):
    response = client.post(reverse('forgot_password'), {'email': user.email}, content_type='application/json')
    assert response.status_code == 200

    token = response.context[0]['token']
    uid = response.context[0]['uid']
    response = client.get(reverse('password_reset_confirm', kwargs={'token': token, 'uidb64': uid}))
    assert response.status_code == 302

    data = {
        'new_password': PASSWORD + "1",
        'new_password_confirm': PASSWORD + "1"
    }
    response = client.post(reverse('forgot_password_handler'),
                           data=data, content_type='application/json')
    assert response.status_code == 201

    response = client.get(reverse('password_reset_confirm', kwargs={'token': token, 'uidb64': uid}))
    assert response.status_code == 400


@pytest.mark.django_db
def test_forgot_password_reset_link_after_user_logged_in(client, user):
    response = client.post(reverse('forgot_password'), {'email': user.email}, content_type='application/json')

    assert response.status_code == 200
    data = {
        "email": user.email,
        "password": PASSWORD
    }
    client.post('/api/v1/user/login/', data=data, content_type='application/json')
    token = response.context[0]['token']
    uid = response.context[0]['uid']
    response = client.get(reverse('password_reset_confirm', kwargs={'token': token, 'uidb64': uid}))

    assert response.status_code == 400
