
from django.test import SimpleTestCase
from django.urls import reverse


class HTMLTests(SimpleTestCase):

    def test_status_code(self):
        response = self.client.get('/html_endpoint/')
        self.assertEquals(response.status_code, 200)

    def test_view_url(self):
        response = self.client.get(reverse('html_endpoint'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('html_endpoint'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_contains_correct_html(self):
        response = self.client.get('/html_endpoint/')
        self.assertContains(response, '<p>Hello we are in react app</p>')

class JSONTests(SimpleTestCase):

    def test_status_code(self):
        response = self.client.get('/jsn_endpoint/')
        self.assertEquals(response.status_code, 200)

    def test_view_url(self):
        response = self.client.get(reverse('jsn_endpoint'))
        self.assertEquals(response.status_code, 200)

    def test_contains_correct_json(self):
        response = self.client.get('/jsn_endpoint/')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'just': 'some data'}
        )


class TXTTests(SimpleTestCase):

    def test_status_code(self):
        response = self.client.get('/txt_endpoint/')
        self.assertEquals(response.status_code, 200)

    def test_view_url(self):
        response = self.client.get(reverse('txt_endpoint'))
        self.assertEquals(response.status_code, 200)

    def test_contains_correct_txt(self):
        response = self.client.get('/txt_endpoint/')
        self.assertEqual(
            str(response.content, encoding='utf8'),
            'Hello, World'
        )



