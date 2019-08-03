import requests


def test_fail():
    response = requests.get('http://127.0.0.1:8000/')
    assert response.status_code == 404
    assert not response.is_redirect


def test_all_articles():
    response = requests.get('http://127.0.0.1:8000/blog/api/v1/articles/')
    response.raise_for_status()
    assert response.status_code == 200
    assert not response.is_redirect
    assert response.headers["Content-Type"] == "application/json"

