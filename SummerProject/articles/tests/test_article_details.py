import pytest
from articles.models import Article


@pytest.fixture()
def new_article():
    return Article.objects.create(title="new title", content="new content")


@pytest.mark.django_db
def test_get(client, new_article):
    response = client.get('/api/v1/articles/{}/'.format(new_article.id))
    assert response.status_code == 200
    assert response.json() == {"title":	new_article.title, "content": new_article.content}
    assert response['custom_id'] == str(new_article.id)
    assert response['Content-Type'] == 'application/json'


@pytest.mark.django_db
def test_put(client, new_article):
    data = {
        "title": "new title",
        "content": "new content"
    }
    response = client.put('/api/v1/articles/{}/'.format(new_article.id), data=data, content_type='application/json')
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/json'

# test delete method
@pytest.mark.django_db
def test_delete(client, new_article):
    response = client.delete('/api/v1/articles/{}/'.format(new_article.id))

    assert response.status_code == 204
