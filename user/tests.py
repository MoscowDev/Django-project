from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User


class TestSignup(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register')

    def test_signup_returns_201(self):
        data = {
            "username": "nnaji_moses",
            "email": "mosesogomegbunam@gmail.com",
            "first_name": "Nnaji",
            "last_name": "Ogomegbunam",
            "phone_number": "08034567891",
            "password": "SecurePass123!"
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            User.objects.filter(username="nnaji_moses").exists()
        )

    def test_signup_returns_400(self):
        data = {
            "username": "invalid_user",
            "email": "invalidemail",
            "first_name": "Nji",
            "last_name": "Ogbunam",
            "phone_number": "0803",
            "password": "123"
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class TestLogin(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login')

        self.user = User.objects.create_user(
            username="nnaji_moses",
            email="mosesogomegbunam@gmail.com",
            first_name="Nnaji",
            last_name="Ogomegbunam",
            password="SecurePass123!"
        )

    def test_login_returns_200(self):
        data = {
            "email": "mosesogomegbunam@gmail.com",
            "password": "SecurePass123!"
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_returns_400(self):
        data = {
            "email": "",
            "password": ""
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)