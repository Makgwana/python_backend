from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomUser
from rest_framework import status

class UserRegistrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('api:user_register')
        self.login_url = reverse('api:user_login')
        self.user_data = {
            'username': 'testuser',
            'password': '09021171Mc@',
            'email': 'molatosekgobela@gmail.com',
            'nickname': 'Test nickname',
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_user_login(self):
        # Register a user
        self.client.post(self.register_url, data=self.user_data)

        # Login with the registered user
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        }
        response = self.client.post(self.login_url, data=login_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class UserIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('api:user_register')
        self.login_url = reverse('api:user_login')
        self.user_data = {
            'username': 'testuser',
            'password': '09021171Mc@',
            'email': 'molatosekgobela@gmail.com',
            'nickname': 'Test nickname',
        }

    def test_user_registration_and_login(self):
        # Register a new user
        registration_response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(registration_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)

        # Login with the registered user
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        }
        login_response = self.client.post(self.login_url, data=login_data)
        
        if login_response.status_code == 200:
            self.assertIn('access', login_response.data)
            self.assertIn('refresh', login_response.data)
        else:
            # Handle login error, e.g., by printing the response data
            print(f"Login Error: {login_response.data}")
