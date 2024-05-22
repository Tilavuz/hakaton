from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import Tuman, Mahalla, Maktab
from adduser.models import Certificate,UserInfo
class StatisticsAPITest(APITestCase):
    def setUp(self):
        Tuman.objects.create(name='Test Tuman', plan_en_b2=10, plan_en_c1=15, plan_en_c2=20, plan_deorother_b2=12, plan_deorother_c1=18, plan_deorother_c2=25)
        Mahalla.objects.create(name='Test Mahalla 1')
        Mahalla.objects.create(name='Test Mahalla 2')
        Maktab.objects.create(name='Test Maktab 1')
        Maktab.objects.create(name='Test Maktab 2')

    def test_statistics(self):
        url = reverse('statistics')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_tuman'], 1)
        self.assertEqual(response.data['total_mahalla'], 2)
        self.assertEqual(response.data['total_maktab'], 2)
        self.assertEqual(response.data['total_plan_en_b2'], 10)
        self.assertEqual(response.data['total_plan_en_c1'], 15)
        self.assertEqual(response.data['total_plan_en_c2'], 20)
        self.assertEqual(response.data['total_plan_deorother_b2'], 12)
        self.assertEqual(response.data['total_plan_deorother_c1'], 18)
        self.assertEqual(response.data['total_plan_deorother_c2'], 25)

class SearchAPITest(APITestCase):
    def setUp(self):
        self.tuman = Tuman.objects.create(name='Test Tuman')
        self.mahalla = Mahalla.objects.create(name='Test Mahalla')
        self.maktab = Maktab.objects.create(name='Test Maktab')

    def test_search(self):
        url = reverse('search')
        data = {'query': 'Test'}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tuman'][0]['name'], 'Test Tuman')
        self.assertEqual(response.data['mahalla'][0]['name'], 'Test Mahalla')
        self.assertEqual(response.data['maktab'][0]['name'], 'Test Maktab')

class MonitoringAPITest(APITestCase):
    def setUp(self):
        self.tuman = Tuman.objects.create(name='Test Tuman')
        self.mahalla = Mahalla.objects.create(name='Test Mahalla')
        self.maktab = Maktab.objects.create(name='Test Maktab')

    def test_monitoring(self):
        url = reverse('monitoring')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['tuman']), 1)
        self.assertEqual(len(response.data['mahalla']), 1)
        self.assertEqual(len(response.data['maktab']), 1)

class OrderingAPITest(APITestCase):
    def setUp(self):
        Tuman.objects.create(name='Test Tuman 1')
        Tuman.objects.create(name='Test Tuman 2')

    def test_ordering(self):
        url = reverse('ordering')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Test Tuman 1')

class UserInfoStatisticsAPITest(APITestCase):
    def setUp(self):
        UserInfo.objects.create(name='Test User 1', lastname='Test Lastname 1', fname='Test Fname 1', school='Test School 1', neighborhood='Test Neighborhood 1', JSHSHIR='Test JSHSHIR 1', phone_number='1234567890')
        Certificate.objects.create(title='Test Certificate 1', overel='Test Level 1')

    def test_userinfo_statistics(self):
        url = reverse('userinfo_statistics')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_users'], 1)
        self.assertEqual(response.data['total_certificates'], 1)

class UserInfoSearchAPITest(APITestCase):
    def setUp(self):
        self.user_info = UserInfo.objects.create(name='Test User', lastname='Test Lastname', fname='Test Fname', school='Test School', neighborhood='Test Neighborhood', JSHSHIR='Test JSHSHIR', phone_number='1234567890')

    def test_userinfo_search(self):
        url = reverse('userinfo_search')
        data = {'query': 'Test'}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Test User')

class UserInfoOrderingAPITest(APITestCase):
    def setUp(self):
        UserInfo.objects.create(name='Test User 1')
        UserInfo.objects.create(name='Test User 2')

    def test_userinfo_ordering(self):
        url = reverse('userinfo_ordering')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Test User 1')

class CertificateMonitoringAPITest(APITestCase):
    def setUp(self):
        Certificate.objects.create(title='Test Certificate 1')

    def test_certificate_monitoring(self):
        url = reverse('certificate_monitoring')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
