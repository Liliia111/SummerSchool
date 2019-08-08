import pytest


@pytest.mark.django_db
def test_fail(client):
    test = client.get('/max')
    assert test.status_code == 404


@pytest.mark.django_db
def test_get_all_articles(client):
    response = client.get('/api/v1/articles/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_article(client):
    data = {
        "title": "fixture title",
        "content": "fixture content"
    }
    response = client.post('/api/v1/articles/', data=data, content_type='application/json')
    assert response.status_code == 200
    assert response.json() == {'created': {"title": "fixture title", "content": "fixture content"}}
