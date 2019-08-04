import pytest
import requests
from blog.models import Article


@pytest.mark.django_db
def test_model():
    article = Article.objects.create(
        title="Sample title",
        content="Sample content"
    )
    assert article.title == "Sample title"
    assert article.content == "Sample content"


def test_get():
    response = requests.get('http://127.0.0.1:8000/api/v1/articles/')
    response.raise_for_status()
    assert response.status_code == 200


def test_post():
    response = requests.post('http://127.0.0.1:8000/api/v1/articles/', json={'title': 'title', 'content': 'content'})
    assert response.status_code == 201
    assert response.json() == {'title': 'sample', 'content': 'sample'}


def test_get_one():
    response = requests.get('http://127.0.0.1:8000/api/v1/articles/1')
    assert response.status_code == 200
    assert response.json() == {
        "title": "Lorem ipsum",
        "content": "Dolor sit amet, turpis non dolor mauris fusce, ac morbi donec suscipit praesent, congue sed, libero tellus malesuada fames lacinia tortor risus, sollicitudin felis pulvinar pulvinar. Massa lectus integer integer orci, leo fermentum integer eu vel nulla, lobortis leo a. Ante nullam justo, hymenaeos lectus eu nunc, lorem aenean tellus mauris fusce leo neque. Dignissim posuere placerat, risus accumsan congue, pharetra varius, eget nec condimentum feugiat neque. Ligula vulputate in molestie urna id elit, magna lectus mauris amet, in integer duis sit pede gravida."

    }


def test_update():
    response = requests.put('http://127.0.0.1:8000/api/v1/articles/4', json={'title': 'lalala', 'content': 'lalala'})
    response.raise_for_status()
    assert response.status_code == 200


def test_delete():
    response = requests.delete('http://127.0.0.1:8000/api/v1/articles/5')
    response.raise_for_status()
    assert response.status_code == 204
