from django.test import Client
import pytest
import json
import requests
from article.models import Article

client = Client()

@pytest.fixture()
def created_article():
    return Article.objects.create(title="Testing", description="My", body="Tests")

@pytest.mark.django_db
def test_get_id_of_article(created_article, client):
    response = client.get('/api/v1/articles/{}'.format(created_article.id))
    assert response.status_code == 200
    assert response.json() == {"article":[{'title': 'Testing', 'description': 'My', 'id': created_article.id, 'body': 'Tests'}]}
    assert response["Content-Type"] == "application/json"


@pytest.mark.django_db
def test_put(created_article, client):
    data = {'title': 'Updated',
            'description': 'Testing',
            'body': 'Test'}
    json_srt = json.dumps(data)

    header = {'Content-Type': 'application/json', 'Accept-Encoding': None}
    response = client.put('/api/v1/articles/{}'.format(created_article.id), headers=header, data=json_srt, verify=False)
    assert response.json() == {"updated":data}
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete(created_article, client):
    response = client.delete('/api/v1/articles/{}'.format(created_article.id))
    assert response.status_code == 204

@pytest.mark.parametrize(
    "title, description, body", [
        ('Fu', 'Ck', 'Off'),
        ('21.08', 'HB', 'ToMe'),
        ('Soft', 'Serve', 'SummerSchool'),
        ('Hello', 'My', 'Dear')
    ]
)
def test_post(db, client, title, description, body):
    data = {"title": title, "description": description, "body": body}
    header = {'Content-Type': 'application/json'}
    response = client.post('/api/v1/articles/', data=data, content_type="application/json")
    assert response.json() == {"created": data}