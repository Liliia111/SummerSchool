import unittest
import requests


class Test(unittest.TestCase):
    def test_json(self):
        tmp = requests.get("http://127.0.0.1:8000/json_test/")
        self.assertEqual(tmp.status_code, 200)
        self.assertFalse(tmp.is_redirect)
        self.assertEqual(tmp.url, "http://127.0.0.1:8000/json_test/")
        self.assertEqual(type(tmp.content), bytes)

    def test_txt(self):
        tmp = requests.get("http://127.0.0.1:8000/txt_test/")
        self.assertEqual(tmp.status_code, 200)
        self.assertFalse(tmp.is_redirect)
        self.assertEqual(tmp.url, "http://127.0.0.1:8000/txt_test/")
        self.assertEqual(type(tmp.text), str)
        self.assertEqual(tmp.text, "txt_Test file")

    def test_html(self):
        tmp = requests.get("http://127.0.0.1:8000/")
        self.assertEqual(tmp.status_code, 200)
        self.assertFalse(tmp.is_redirect)
        self.assertEqual(tmp.url, "http://127.0.0.1:8000/")
        self.assertEqual(tmp.headers['Content-Type'], "text/html; charset=utf-8")
