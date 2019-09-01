import pytest
from article.models import Article, Comment
from user.models import User
import random
import string


@pytest.fixture()
def create_user(db):
    def inner():
        password = "44456"
        user = User.objects.create(first_name="First",
                                   last_name="Last",
                                   email="{}@mail.com".
                                   format(''.join([random.choice(string.ascii_lowercase) for n in range(10)])),
                                   password=password)
        return user, password
    return inner  # provide the fixture value


# @pytest.fixture()
# def get_user(create_user):
#     username, password = create_user()
#     return username, password
#
#
# user_name, user_password = get_user()

class NewUser:
    @pytest.fixture(autouse=True)
    def get_user(self, create_user):
        username, password = create_user()
        return username, password

    def __init__(self, get_user):
        self.user_name, self.user_password = get_user()

    def user_name(self):
        return self.user_name

    def user_password(self):
        return self.user_password


@pytest.fixture()
def new_article(db):
    new_user = NewUser()
    print("new_user{}".format(new_user))
    return Article.objects.create(
        headline="New one",
        photo="https://oyebesmartest.com/public/uploads/preview/-11550470501p1ok6amcue.png",
        video="https://www.youtube.com/watch?v=axsaC62UQOc",
        # error with User instance
        author=new_user.user_name(),
        source="New's",
        content="Some new content")


@pytest.mark.djago_db
def test_comment_post(client, new_article):
    new_user = NewUser()
    data = {
        'content': "This is new comment"
    }
    print(new_user.user_name(), new_user.user_password())
    client.login(username=new_user.user_name(), password=new_user.user_password())

    response = client.post('/api/v1/articles/{}/comment/'.format(new_article.id),
                           data=data,
                           content_type='application/json')
    comment = new_article.comments.get(id=1)
    assert response.status_code == 201
    assert response['Content-Type'] == 'application/json'
    assert response['comment_id'] == comment.id
