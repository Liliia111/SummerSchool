import pytest
from blog.models import Article

PYTESTMARK = pytest.mark.django_db


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
    response = client.post('/api/v1/articles/', {'title': 'title', 'content': 'content98798'},
                           content_type='application/json')
    assert response.status_code == 201
    assert response.json() == {'title': 'title', 'content': 'content98798'}


@pytest.mark.parametrize(
    'title, content', [
        ('jj' * 300, '1'),
        (0.3, None),
    ]
)
def test_post_not_valid_data(client, title, content):
    response = client.post('/api/v1/articles/', {'title': title, 'content': content},
                           content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {"error": "not valid data"}
    assert Article.objects.count() == 0
