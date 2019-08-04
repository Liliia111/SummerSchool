import unittest
import requests


class Test(unittest.TestCase):
    def test_get(self):
        tmp = requests.get("http://127.0.0.1:8000/api/v1/articles/")
        self.assertEqual(tmp.status_code, 200)
        self.assertFalse(tmp.is_redirect)
        self.assertEqual(tmp.headers['Content-Type'], "application/json")

    def test_post(self):
        tmp = requests.post("http://127.0.0.1:8000/api/v1/articles/", json={"title": "new_title", "content": "new_content"})
        self.assertEqual(tmp.status_code, 201)
        self.assertFalse(tmp.is_redirect)
        self.assertEqual(tmp.headers['Content-Type'], "application/json")
        # self.assertEqual(tmp.text, {"title": "new_title", "content": "new_content"})