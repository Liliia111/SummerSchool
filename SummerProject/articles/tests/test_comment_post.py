import pytest
from articles.models import Article, Comment
from user.models import User
import random
import string


''' Login'''
@pytest.fixture()
def create_user(db, client):
    def inner():
        email = "{}@mail.com".format(''.join([random.choice(string.ascii_lowercase) for n in range(10)]))
        password = "44456"
        client.post('/api/v1/user/registration/', data={'first_name': 'Max',
                                                        'last_name': 'NewMax',
                                                        'email': email,
                                                        'password': password}, content_type='application/json')
        client.post('/api/v1/user/login/', data={'email': email,
                                                 'password': password}, content_type='application/json')
        user = User.objects.get(email=email)

        return user, password
    return inner


@pytest.fixture()
def new_article(db, create_user):
    new_user, _ = create_user()
    return Article.objects.create(
        headline="New one",
        photo="http://fake_photo.png",
        video="http://fake_video",
        author=new_user,
        source="New's",
        content="Some new content")


@pytest.mark.django_db
def test_comment_post(client, new_article):
    data = {
        'content': "This is new comment"
    }
    response = client.post('/api/v1/articles/{}/comments/'.format(new_article.id),
                           data=data,
                           content_type='application/json')
    comment = new_article.comments.get(id=response['comment_id'])
    assert response.status_code == 201
    assert response['Content-Type'] == 'text/html; charset=utf-8'
    assert comment.content == 'This is new comment'