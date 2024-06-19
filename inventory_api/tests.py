from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Item
from rest_framework.authtoken.models import Token

class InventoryApiTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.item_data = {
            'name': 'Test Item',
            'description': 'This is a test item.',
            'quantity': 10,
            'price': '99.99'
        }

        self.item = Item.objects.create(**self.item_data)

        self.item_list_url = reverse('item-list-create')
        self.item_detail_url = reverse('item-detail', kwargs={'pk': self.item.id})

    def test_create_item(self):
        response = self.client.post(self.item_list_url, {
            'name': 'New Item',
            'description': 'This is a new item.',
            'quantity': 5,
            'price': '49.99'
        }, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)
        new_item = Item.objects.filter(name='New Item').first()
        self.assertIsNotNone(new_item)
        self.assertEqual(new_item.name, 'New Item')

    def test_get_all_items(self):
        response = self.client.get(self.item_list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.item.name)

    def test_get_single_item(self):
        response = self.client.get(self.item_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_update_item(self):
        response = self.client.put(self.item_detail_url, {
            'name': 'Updated Item',
            'description': 'This is an updated item.',
            'quantity': 15,
            'price': '149.99'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_item = Item.objects.get(id=self.item.id)
        self.assertEqual(updated_item.name, 'Updated Item')
        self.assertEqual(updated_item.quantity, 15)

    def test_partial_update_item(self):
        response = self.client.patch(self.item_detail_url, {
            'quantity': 20
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_item = Item.objects.get(id=self.item.id)
        self.assertEqual(updated_item.quantity, 20)

    def test_delete_item(self):
        response = self.client.delete(self.item_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        deleted_item = Item.objects.get(id=self.item.id)
        self.assertTrue(deleted_item.is_deleted)

    def test_create_item_invalid_data(self):
        response = self.client.post(self.item_list_url, {
            'name': '',
            'description': 'This is a new item with invalid data.',
            'quantity': -5,
            'price': 'invalid_price'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_item_invalid_data(self):
        response = self.client.put(self.item_detail_url, {
            'name': '',
            'description': 'This is an updated item with invalid data.',
            'quantity': -10,
            'price': 'invalid_price'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
