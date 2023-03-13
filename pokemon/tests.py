from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

class DjoserTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_registration(self):
        response = self.client.post('/auth/users/', {
            'username': 'test',
            'password': 'testpassword',
            're_password': 'testpassword',
        })

        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.test_registration()

        response = self.client.post('/auth/jwt/create/', {
            'username': 'test',
            'password': 'testpassword',
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
