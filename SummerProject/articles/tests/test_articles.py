import pytest
from articles.models import Article


@pytest.fixture()
def new_article():
    return Article.objects.create(title="new title", content="new content")


@pytest.mark.django_db
def test_fail(client):
    test = client.get('/max')
    assert test.status_code == 404


@pytest.mark.django_db
def test_get(client):
    response = client.get('/api/v1/articles/')
    assert response.status_code == 200
    assert response['Content-Type'] == "text/html; charset=utf-8"
    assert response['custom'] == "custom get articles"


@pytest.mark.parametrize("title_text, content_text", [
    ("title" * 10, "content" * 50),
    ("title" * 25, "content" * 100),
    ("title" * 70, "content" * 300),
    ("title" * 125, "content" * 700)
])
@ pytest.mark.django_db
def test_post(client, title_text, content_text, ):
    data = {
        "title": title_text,
        "content": content_text
    }
    response = client.post('/api/v1/articles/', data=data, content_type='application/json')
    if len(data['title']) > 300:
        assert response.status_code == 400
    else:
        assert response.status_code == 201
        assert response["Content-Type"] == "application/json"
