import pytest
import requests
from blog.models import Article

PYTESTMARK = pytest.mark.django_db


@pytest.fixture
def existing_article():
    article = Article.objects.create(
        title="title",
        content="content"
    )
    return article


def test_get_by_id(client, existing_article):
    response = client.get('/api/v1/articles/{}'.format(existing_article.id))
    assert response.status_code == 200
    assert response.json() == {'title': 'title', 'content': 'content'}


def test_get_by_nonexistent_id(client):
    response = client.get('/api/v1/articles/{}'.format(0))
    assert response.status_code == 404
    assert response.json() == {'error': "primary key does not exist"}


def test_update(client, existing_article):
    response = client.put('/api/v1/articles/{}'.format(existing_article.id),
                          {'title': 'lalala', 'content': 'lalala'}, content_type='application/json')
    assert response.status_code == 201
    assert response.json() == {'title': 'lalala', 'content': 'lalala'}


def test_update_by_nonexistent_id(client):
    response = client.put('/api/v1/articles/{}'.format(0), {'title': 'lalala', 'content': 'lalala'},
                          content_type='application/json')
    assert response.status_code == 404
    assert response.json() == {'error': "primary key does not exist"}


@pytest.mark.parametrize(
    'title, content', [
        ('jj' * 300, '1'),
        (0.3, None),
    ]
)
def test_update_with_invalid_data(client, existing_article, title, content):
    response = client.put('/api/v1/articles/{}'.format(existing_article.id),
                          {'title': title, 'content': content},
                          content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': "not valid data"}


def test_delete(client, existing_article):
    response = client.delete('/api/v1/articles/{}'.format(existing_article.id))
    assert response.status_code == 204


def test_delete_by_nonexistent_id(client):
    response = client.delete('/api/v1/articles/{}'.format(0))
    assert response.status_code == 404
    assert response.json() == {'error': "primary key does not exist"}
