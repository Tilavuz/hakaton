from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Viloyat, Tuman, Mahalla, Maktab, User

class ViloyatModelTest(TestCase):
    def test_valid_viloyat(self):
        viloyat = Viloyat(
            name="Test Region",
            overall=100,
            plan_en_b2=10,
            plan_en_c1=20,
            plan_en_c2=30,
            plan_deorother_b2=10,
            plan_deorother_c1=20,
            plan_deorother_c2=10,
        )
        viloyat.clean()
        viloyat.save()
        self.assertEqual(Viloyat.objects.count(), 1)

    def test_invalid_viloyat_exceeding_plans(self):
        viloyat = Viloyat(
            name="Test Region",
            overall=50,
            plan_en_b2=20,
            plan_en_c1=20,
            plan_en_c2=20,
            plan_deorother_b2=10,
            plan_deorother_c1=10,
            plan_deorother_c2=10,
        )
        with self.assertRaises(ValidationError):
            viloyat.clean()

class TumanModelTest(TestCase):
    def test_valid_tuman(self):
        tuman = Tuman(
            name="Test District",
            overall=100,
            plan_en_b2=10,
            plan_en_c1=20,
            plan_en_c2=30,
            plan_deorother_b2=10,
            plan_deorother_c1=20,
            plan_deorother_c2=10,
        )
        tuman.clean()
        tuman.save()
        self.assertEqual(Tuman.objects.count(), 1)

    def test_invalid_tuman_exceeding_plans(self):
        tuman = Tuman(
            name="Test District",
            overall=50,
            plan_en_b2=20,
            plan_en_c1=20,
            plan_en_c2=20,
            plan_deorother_b2=10,
            plan_deorother_c1=10,
            plan_deorother_c2=10,
        )
        with self.assertRaises(ValidationError):
            tuman.clean()

class MahallaModelTest(TestCase):
    def setUp(self):
        self.tuman = Tuman.objects.create(
            name="Test District",
            overall=100,
            plan_en_b2=10,
            plan_en_c1=20,
            plan_en_c2=30,
            plan_deorother_b2=10,
            plan_deorother_c1=20,
            plan_deorother_c2=10,
        )

    def test_valid_mahalla(self):
        mahalla = Mahalla(
            name="Test Community",
            tuman=self.tuman,
            overall=100,
            plan_en_b2=10,
            plan_en_c1=20,
            plan_en_c2=30,
            plan_deorother_b2=10,
            plan_deorother_c1=20,
            plan_deorother_c2=10,
        )
        mahalla.clean()
        mahalla.save()
        self.assertEqual(Mahalla.objects.count(), 1)

    def test_invalid_mahalla_exceeding_plans(self):
        mahalla = Mahalla(
            name="Test Community",
            tuman=self.tuman,
            overall=50,
            plan_en_b2=20,
            plan_en_c1=20,
            plan_en_c2=20,
            plan_deorother_b2=10,
            plan_deorother_c1=10,
            plan_deorother_c2=10,
        )
        with self.assertRaises(ValidationError):
            mahalla.clean()

class MaktabModelTest(TestCase):
    def setUp(self):
        self.tuman = Tuman.objects.create(
            name="Test District",
            overall=100,
            plan_en_b2=10,
            plan_en_c1=20,
            plan_en_c2=30,
            plan_deorother_b2=10,
            plan_deorother_c1=20,
            plan_deorother_c2=10,
        )
        self.mahalla = Mahalla.objects.create(
            name="Test Community",
            tuman=self.tuman,
            overall=100,
            plan_en_b2=10,
            plan_en_c1=20,
            plan_en_c2=30,
            plan_deorother_b2=10,
            plan_deorother_c1=20,
            plan_deorother_c2=10,
        )

    def test_valid_maktab(self):
        maktab = Maktab(
            name="Test School",
            tuman=self.tuman,
            mahalla=self.mahalla,
            overall=100,
            plan_en_b2=10,
            plan_en_c1=20,
            plan_en_c2=30,
            plan_deorother_b2=10,
            plan_deorother_c1=20,
            plan_deorother_c2=10,
        )
        maktab.clean()
        maktab.save()
        self.assertEqual(Maktab.objects.count(), 1)

    def test_invalid_maktab_exceeding_plans(self):
        maktab = Maktab(
            name="Test School",
            tuman=self.tuman,
            mahalla=self.mahalla,
            overall=50,
            plan_en_b2=20,
            plan_en_c1=20,
            plan_en_c2=20,
            plan_deorother_b2=10,
            plan_deorother_c1=10,
            plan_deorother_c2=10,
        )
        with self.assertRaises(ValidationError):
            maktab.clean()

class UserModelTest(TestCase):
    def setUp(self):
        self.tuman = Tuman.objects.create(
            name="Test District",
            overall=100,
            plan_en_b2=10,
            plan_en_c1=20,
            plan_en_c2=30,
            plan_deorother_b2=10,
            plan_deorother_c1=20,
            plan_deorother_c2=10,
        )

    def test_create_user_with_valid_role(self):
        user = User.objects.create_user(
            username="testuser",
            password="password123",
            first_name="Test",
            last_name="User",
            role=User.ROLE_TUMAN_MASUL,
            tuman=self.tuman,
        )
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.role, User.ROLE_TUMAN_MASUL)

    def test_create_user_without_tuman(self):
        user = User.objects.create_user(
            username="testuser2",
            password="password123",
            first_name="Test",
            last_name="User",
            role=User.ROLE_ADMIN,
        )
        self.assertEqual(User.objects.count(), 1)
        self.assertIsNone(user.tuman)
