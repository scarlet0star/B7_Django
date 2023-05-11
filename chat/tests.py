from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from chat.models import Room, RoomJoin
from users.models import User
from django.urls import reverse


class Test(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'email': 'test@test.com', 'password': '1234'}
        cls.user = User.objects.create_user(email='test@test.com', password='1234', name="testUser")

    def test_case_rooms(self):
        user_email = 'test3@test.com'
        user_password = 'test'
        user_name = 'testUser3'
        user_data = {'email': user_email, 'password': user_password, "name": user_name}
        user1 = User.objects.create_user(email=user_email, password=user_password, name=user_name)
        user2 = User.objects.create_user(email="test2@test.com", password="test", name="testUser2")
        access_token = self.client.post(reverse('token_obtain_pair'), user_data).data['access']
        url = reverse("room_view")
        token = f'Bearer {access_token}'
        data = {"user": user1.id, "author": user2.id}
        temp = self.client.post(path=url, data=data, headers={'Authorization': token})
        self.assertEqual(temp.status_code, 200)
        result = self.client.get(path=url, headers={'Authorization': token})
        self.assertEqual(result.status_code, 200)

