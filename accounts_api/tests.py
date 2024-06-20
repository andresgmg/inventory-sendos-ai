from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AccountsApiTests(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.username = "testuser"
        self.password = "testpassword"
        self.email = "test@example.com"
        self.user_data = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
        }
        self.user = User.objects.create_user(**self.user_data)
        self.token = Token.objects.create(user=self.user)

    def test_register_user(self):
        unique_username = self.username + "2"
        user_data = {
            "username": unique_username,
            "password": self.password,
            "email": self.email,
        }
        response = self.client.post(self.register_url, user_data, format="json")
        if (
            response.status_code == status.HTTP_301_MOVED_PERMANENTLY
            or response.status_code == status.HTTP_302_FOUND
        ):
            response = self.client.post(response.url, user_data, format="json")
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        new_user = User.objects.get(username=unique_username)
        self.assertEqual(new_user.username, unique_username)

    def test_login_user(self):
        response = self.client.post(
            self.login_url,
            {"username": self.username, "password": self.password},
            format="json",
        )
        if (
            response.status_code == status.HTTP_301_MOVED_PERMANENTLY
            or response.status_code == status.HTTP_302_FOUND
        ):
            response = self.client.post(
                response.url,
                {"username": self.username, "password": self.password},
                format="json",
            )
        if response.status_code != status.HTTP_200_OK:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_login_user_invalid_credentials(self):
        response = self.client.post(
            self.login_url,
            {"username": self.username, "password": "wrongpassword"},
            format="json",
        )
        if (
            response.status_code == status.HTTP_301_MOVED_PERMANENTLY
            or response.status_code == status.HTTP_302_FOUND
        ):
            response = self.client.post(
                response.url,
                {"username": self.username, "password": "wrongpassword"},
                format="json",
            )
        if response.status_code != status.HTTP_400_BAD_REQUEST:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
