import pytest


def test_get_by_pk(client):
    # data = {
    #     'title': 'new title',
    #     'content': 'new content'
    # }
    # posting = client.post('api/v1/articles/', data=data, type='')
    response = client.get('api/v1/articles/')
    assert response.status_code == 200
    # assert response.json() == {"title":	"new title", "content": "new content"}

