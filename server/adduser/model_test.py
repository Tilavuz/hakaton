from django.test import TestCase
from django.core.exceptions import ValidationError
from accounts.models import Tuman, Mahalla, Maktab
from .models import UserInfo, Certificate

class UserInfoModelTest(TestCase):
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

    def test_user_info_creation(self):
        self.assertEqual(self.user_info.name, "John")
        self.assertEqual(self.user_info.language, "english")
        self.assertEqual(self.user_info.status, "uqimoqda")
        self.assertEqual(UserInfo.objects.count(), 1)

    def test_user_info_str(self):
        self.assertEqual(str(self.user_info), "John Doe")

class CertificateModelTest(TestCase):
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
        self.certificate = Certificate.objects.create(
            user_info=self.user_info,
            language="english",
            overall="B2",
            url="http://example.com/certificate"
        )

    def test_certificate_creation(self):
        self.assertEqual(self.certificate.language, "english")
        self.assertEqual(self.certificate.overall, "B2")
        self.assertEqual(Certificate.objects.count(), 1)

    def test_certificate_str(self):
        self.assertEqual(str(self.certificate), "John's Certificate (english - B2)")
