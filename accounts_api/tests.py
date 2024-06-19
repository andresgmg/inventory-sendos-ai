from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AccountsApiTests(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_url = reverse('user')
        self.username = 'testuser'
        self.password = 'testpassword'
        self.email = 'test@example.com'
        self.user_data = {
            'username': self.username,
            'password': self.password,
            'email': self.email
        }
        self.user = User.objects.create_user(**self.user_data)
        self.token = Token.objects.create(user=self.user)

    def test_register_user(self):
        unique_username = self.username + '2'
        user_data = {
            'username': unique_username,
            'password': self.password,
            'email': self.email
        }
        response = self.client.post(self.register_url, user_data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        new_user = User.objects.get(username=unique_username)
        self.assertEqual(new_user.username, unique_username)

    def test_login_user(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        }, format='json')
        if response.status_code != status.HTTP_200_OK:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_get_user_details(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.user_url, format='json')
        if response.status_code != status.HTTP_200_OK:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.username)

    def test_logout_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.logout_url, format='json')
        if response.status_code != status.HTTP_204_NO_CONTENT:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_user_details(self):
        response = self.client.get(self.user_url, format='json')
        if response.status_code != status.HTTP_401_UNAUTHORIZED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
