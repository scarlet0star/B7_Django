from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse


class TestUserToggle(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='testuser@email.com',
            password='testpass123',
            name="name"
        )
        self.admin = get_user_model().objects.create_superuser(
            email='adminuser@email.com',
            password='adminpass123',
            name="name1"
        )
        self.client.force_authenticate(user=self.admin)

    def test_toggle_is_admin(self):
        self.client.login(email='adminuser@email.com', password='adminpass123')
        url = reverse('admin', kwargs={'pk': self.user.pk})
        response = self.client.put(url)
        self.user.refresh_from_db()  # Refresh user object after PUT request
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user.is_admin)

    def test_toggle_is_active(self):
        self.client.login(email='adminuser@email.com', password='adminpass123')
        url = reverse('active', kwargs={'pk': self.user.pk})
        response = self.client.put(url)
        self.user.refresh_from_db()  # Refresh user object after PUT request
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user.is_active)
