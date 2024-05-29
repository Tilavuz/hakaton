from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            first_name="Test",
            last_name="User",
            role=User.ROLE_MAKTAB_MASUL,
            rank=1,
        )
        self.url_login = reverse('login')
        self.url_logout = reverse('logout')
        self.client = APIClient()

    def test_login_success(self):
        response = self.client.post(self.url_login, {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)
        self.assertIn('user', response.data)

    def test_login_failure(self):
        response = self.client.post(self.url_login, {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)

    def test_logout_success(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.post(self.url_logout, {
            'refresh_token': str(refresh)
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], "User logged out successfully.")

    def test_logout_without_refresh_token(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.post(self.url_logout, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "Refresh token is required.")


class UserViewSetTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
            first_name="Admin",
            last_name="User",
            role=User.ROLE_ADMIN,
            rank=4,
        )
        self.tuman_user = User.objects.create_user(
            username="tuman",
            password="tumanpassword",
            first_name="Tuman",
            last_name="User",
            role=User.ROLE_TUMAN_MASUL,
            rank=2,
        )
        self.client = APIClient()
        self.url_user_list = reverse('user-list')

    def test_admin_can_create_user(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(self.url_user_list, {
            'username': 'newuser',
            'password': 'newpassword',
            'first_name': 'New',
            'last_name': 'User',
            'role': User.ROLE_HOKIM,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(response.data['username'], 'newuser')

    def test_tuman_user_cannot_create_higher_rank_user(self):
        self.client.force_authenticate(user=self.tuman_user)
        response = self.client.post(self.url_user_list, {
            'username': 'newuser',
            'password': 'newpassword',
            'first_name': 'New',
            'last_name': 'User',
            'role': User.ROLE_HOKIM,
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("You don't have permission to create a user with this role.", response.data['detail'])

    def test_admin_can_view_all_users(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.url_user_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_tuman_user_can_view_users_with_lower_or_equal_rank(self):
        self.client.force_authenticate(user=self.tuman_user)
        response = self.client.get(self.url_user_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['username'], 'tuman')

