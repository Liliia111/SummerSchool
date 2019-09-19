import pytest
from user.models import User

PASSWORD = "testPassword"


@pytest.fixture()
def user():
    return User.create(first_name="Name", last_name="Last", email="test@test.com", password=PASSWORD)


@pytest.mark.django_db
def test_registration_new_user(client):
    data = {
        "first_name": "Andrii",
        "last_name": "Stasiuk",
        "email": "andrr@gmail.com",
        "password": "12345asdf"
    }
    response = client.post('/api/v1/user/registration/', data=data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_registration_new_user_via_facebook(client):
    data = {
        "first_name": "Andrii",
        "last_name": "Stasiuk",
        "userId": "1234567889753",
    }
    response = client.post('/api/v1/user/facebook_registration/', data=data, content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_registration_user_with_existing_id(client, user):
    data = {
        "first_name": "Andrii",
        "last_name": "Stasiuk",
        "userId": "test@test.com",
    }
    response = client.post('/api/v1/user/facebook_registration/', data=data, content_type='application/json')
    assert response.status_code == 100


@pytest.mark.parametrize("first_name, last_name, email, password", [
    ("", "", "", ""),
    ("Andrii", "Stasiuk", "asdads", "asdassd"),
    ("Andrii", "Stasiuk", "asdads@gmail.com", "asd")
])
@pytest.mark.django_db
def test_registration_with_invalid_data(client, first_name, last_name, email, password):
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password
    }
    response = client.post('/api/v1/user/registration/', data=data, content_type='application/json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_login(client, user):
    data = {
        "email": user.email,
        "password": PASSWORD
    }
    response = client.post('/api/v1/user/login/', data=data, content_type='application/json')
    assert response.status_code == 200
    assert 'sessionid' in response.cookies
    assert response.cookies['sessionid'] is not None
    assert 'csrftoken' in response.cookies


@pytest.mark.django_db
def test_failed_login(client, user):
    data = {
        "email": user.email,
        "password": PASSWORD + "1"
    }
    response = client.post('/api/v1/user/login/', data=data, content_type='application/json')
    assert response.status_code == 400
    assert 'sessionid' not in response.cookies


@pytest.mark.django_db
def test_logout(client):
    response1 = client.get('/api/v1/user/logout/')
    assert response1.status_code == 200


@pytest.mark.django_db
def test_change_data(client, user):
    data = {
        "first_name": "Andrew",
        "last_name": "New"
    }
    data1 = {
        "email": user.email,
        "password": PASSWORD
    }
    client.post('/api/v1/user/login/', data=data1, content_type='application/json')
    response = client.put('/api/v1/user/self/', data=data, content_type='application/json')
    assert response.status_code == 200
