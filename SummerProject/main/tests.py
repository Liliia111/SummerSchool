import unittest
import requests
from ast import literal_eval
class MyTestCase(unittest.TestCase):
    def test_error(self):
        response = requests.get('http://localhost:8000/error')
        self.assertEqual(response.status_code, 404)
    def htmltest(self):
        response = requests.get('http://localhost:8000/')
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('<title>React App</title>', html)

    def jsontest(self):
        response = requests.get('http://localhost:8000/json_bitch')
        data = literal_eval(response.content.decode('utf8'))
        self.assertEqual(data["Porn"], "Hub")
    def txttest(self):
        response = requests.get('http://localhost:8000/random_string')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'random_string/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()
