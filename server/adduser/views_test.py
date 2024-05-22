from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import Tuman, Mahalla, Maktab
from .models import UserInfo

class StudentViewSetTest(APITestCase):
    def setUp(self):
        self.tuman = Tuman.objects.create(name="Test Tuman")
        self.mahalla = Mahalla.objects.create(name="Test Mahalla")
        self.maktab = Maktab.objects.create(name="Test Maktab")
        self.user_info = UserInfo.objects.create(
            name="John",
            lastname="Doe",
            fname="Jonathan",
            school=self.maktab,
            neighborhood=self.mahalla,
            tuman=self.tuman,
            JSHSHIR="12345678901234567890",
            phone_number="1234567890",
            language="english",
            status="uqimoqda",
        )
        self.list_url = reverse('userinfo-list')  # Update 'userinfo-list' to the name of your route

    def test_list_users(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "John")

    def test_create_user(self):
        data = {
            "name": "Jane",
            "lastname": "Doe",
            "fname": "Janet",
            "school": self.maktab.id,
            "neighborhood": self.mahalla.id,
            "tuman": self.tuman.id,
            "JSHSHIR": "09876543210987654321",
            "phone_number": "0987654321",
            "language": "english",
            "status": "uqimoqda",
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserInfo.objects.count(), 2)
        self.assertEqual(UserInfo.objects.last().name, "Jane")
