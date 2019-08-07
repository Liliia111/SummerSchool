import pytest
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
    response = client.post('/api/v1/articles/', {'title': 'title', 'content': 'content98798'},
                           content_type='application/json')
    assert response.status_code == 200
    assert response.json() == {'title': 'title', 'content': 'content98798'}


@pytest.mark.parametrize(
    'title, content', [
        ('jj', '1'),
        (0.3, ''),
        ('5', 'Buzz'),
        ('10', 'Buzz'),
        ('15', 'FizzBuzz'),
        ('16', '16')
    ]
)
# @pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
def test_input_for_db(title, content):
    article = Article.objects.create(title=title, content=content)
    assert article.title == title
    assert article.content == content






