import pytest
from article.models import Article, Comment
from user.models import User
from django.forms.models import model_to_dict
from mixer.backend.django import mixer
import random
import string

ARTICLES_NUMBER = 4
COMMENTS_NUMBER = 4
ARTICLES_AMOUNT = 3


''' Registration and Login'''
@pytest.fixture
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

        return user
    return inner


@pytest.fixture
def new_comment(db, create_user):
    new_user = create_user()
    return Comment.objects.create(
        user=new_user,
        content=''.join([random.choice(string.ascii_lowercase) for n in range(25)])
    )


@pytest.fixture
def new_article(db, create_user):
    new_user = create_user()
    return Article.objects.create(
        headline=''.join([random.choice(string.ascii_lowercase) for n in range(30)]),
        photo="http://fake_photo.png",
        video="http://fake_video",
        author=new_user,
        source="New's",
        content=''.join([random.choice(string.ascii_lowercase) for n in range(50)]))


# mb create function that will be create a list of list elems that then will be attached to each art


@pytest.fixture
def create_articles(new_article, new_comment, create_user):
    comments_number = COMMENTS_NUMBER
    new_user = create_user()
    articles = list()
    for art in range(ARTICLES_NUMBER):
        article = mixer.blend(Article, author=new_user)
        print()
        for cmnt in range(comments_number):
            comment = mixer.blend(Comment, user=new_user)
            article.comments.add(comment)
        articles.append(model_to_dict(article))
        comments_number = comments_number - 1

    return articles


@pytest.mark.django_db
def test_most_commented(client, create_articles):
    # in create articles only one article obj is created as well as comment despite for
    # only old obj
    articles = create_articles
    response = client.get('/api/v1/articles/most_commented/')
    assert response.json()[0]['art_comments'] == len(articles[0]['comments'])
    assert len(response.json()) == ARTICLES_AMOUNT
    assert response.status_code == 200
    assert response['content-type'] == "text/html; charset=utf-8"
