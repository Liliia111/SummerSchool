import requests


def test_get_all_articles():
    get_request = requests.get('http://127.0.0.1:8000/api/v1/articles/')
    get_request.raise_for_status()
    assert get_request.status_code == 200
    assert not get_request.is_redirect
    assert get_request.headers["Content-Type"] == "application/json"



def test_get_article_by_id():
    response = requests.get('http://127.0.0.1:8000/api/v1/articles/3')
    assert response.status_code == 200
    assert response.json() == {
        "title": "Lorem Ipsum",
        "content": "AAAAAAAAAAAAAAAAAAAA"
    }


def test_create_item():
    response = requests.post(
        "http://127.0.0.1:8000/api/v1/articles/", json={
            "title": "Bazz",
            "content": "Drop the bazz"
        }
    )
    # 2xx codes = success
    assert response.status_code == 201
    assert response.json() == {
        "title": "Bazz",
        "content": "Drop the bazz"
    }


def test_delete():
    response = requests.post(
        "http://127.0.0.1:8000/api/v1/articles/", json={
            "title": "Bazz",
            "content": "Drop the bazz"
        }
    )
    # 2xx codes = success
    response.raise_for_status()
    assert response.status_code == 201
    response = requests.delete("http://127.0.0.1:8000/api/v1/articles/3")
    response.raise_for_status()
    assert response.status_code == 204