import pytest
import requests
from blog.models import Article

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_model():
    article = Article.objects.create(
        title="Sample title",
        content="Sample content"
    )
    assert article.title == "Sample title"
    assert article.content == "Sample content"


def test_get(client):
    response = client.get('/api/v1/articles/')
    assert response.status_code == 200


def test_post(client):
    response = client.post('/api/v1/articles/', {'title': 'title', 'content': 'content98798'}, content_type='application/json')
    assert response.status_code == 201
    assert response.json() == {'title': 'title', 'content': 'content98798'}


def test_get_one(client):
    client.post('/api/v1/articles/', {'title': 'title', 'content': 'content98798'}, content_type='application/json')
    response = client.get('/api/v1/articles/1')
    assert response.status_code == 200
    assert response.json() == {'title': 'title', 'content': 'content98798'}

#
# def test_update():
#     response = requests.put('http://127.0.0.1:8000/api/v1/articles/4', json={'title': 'lalala', 'content': 'lalala'})
#     response.raise_for_status()
#     assert response.status_code == 200
#
#
# def test_delete():
#     response = requests.delete('http://127.0.0.1:8000/api/v1/articles/5')
#     response.raise_for_status()
#     assert response.status_code == 204
