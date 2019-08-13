import pytest
import pdb


@pytest.mark.django_db
def test_create_new_user(client):
    data = {
        "first_name": "User",
        "last_name": "Test",
        "email": "user@gmail.com",
        "password": "user12345"
    }

    response = client.post('/api/v1/auth/registration/', data=data, content_type="application/json")

    assert response.status_code == 201
