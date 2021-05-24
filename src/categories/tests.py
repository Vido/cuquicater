from django.test import Client
from django.test import TestCase

class CategoriesTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        response = self.client.get('/categories.json')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(len(response.context['customers']), 5)


class BrandsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/brands.json')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(len(response.context['customers']), 5)
