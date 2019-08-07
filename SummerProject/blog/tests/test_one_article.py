import pytest
import requests
from blog.models import Article

pytestmark = pytest.mark.django_db


@pytest.fixture
def existing_article():
    article = Article.objects.create(
        title="title",
        content="content"
    )
    return article


def test_get_one(client, existing_article):
    # client.post('/api/v1/articles/', {'title': 'title', 'content': 'content'}, content_type='application/json')

    response = client.get('/api/v1/articles/{}'.format(existing_article.id))
    assert response.status_code == 200
    assert response.json() == {'title': 'title', 'content': 'content'}


def test_update(client, existing_article):

    response = client.put('/api/v1/articles/{}'.format(existing_article.id), {'title': 'lalala', 'content': 'lalala'},
                          content_type='application/json')
    assert response.json() == {'title': 'lalala', 'content': 'lalala'}
    assert response.status_code == 200


def test_delete(client, existing_article):


    response = client.delete('/api/v1/articles/{}'.format(existing_article.id))
    assert response.status_code == 204
