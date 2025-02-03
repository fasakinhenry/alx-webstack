import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class UserViewsTestCase(TestCase):
    """Test case for user views."""

    def setUp(self):
        """Set up the test environment."""
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')

        self.user_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'testuser@example.com'
        }

    def test_register_view_post_success(self):
        """Test registration with valid data."""
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_view_post_invalid(self):
        """Test registration with invalid data."""
        invalid_data = self.user_data.copy()
        invalid_data['password2'] = 'mismatch'
        response = self.client.post(self.register_url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_register_view_get(self):
        """Test GET request to the register view."""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_view_post_success(self):
        """Test login with valid credentials."""
        user = User.objects.create_user(
            username='testuser', password='testpassword123')
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.home_url)

    def test_login_view_post_invalid(self):
        """Test login with invalid credentials."""
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(msg.message == 'Invalid username or password.' for msg in messages))

    def test_login_view_get(self):
        """Test GET request to the login view."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_view(self):
        """Test logout functionality."""
        user = User.objects.create_user(
            username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('landpage'))
