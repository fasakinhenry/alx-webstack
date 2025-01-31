from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse                                                          
from clients.forms import UserRegistrationForm                      
from clients.models import Profile


class LoginViewTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.username = 'testuser'
        self.password = 'testpassword123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client = Client()
        self.login_url = reverse('login')
        self.dashboard_url = reverse('dashboard')

    def test_successful_login(self):
        """Test if login is successful with correct credentials."""
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, self.dashboard_url)

    def test_invalid_login(self):
        """Test login with invalid credentials."""
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertContains(response, 'Invalid username or password.')
        self.assertEqual(response.status_code, 200)

    def test_missing_fields(self):
        """Test login with missing username or password."""
        # Missing username
        response = self.client.post(self.login_url, {
            'password': self.password
        })
        self.assertContains(response, 'Both username and password are required.')
        
        # Missing password
        response = self.client.post(self.login_url, {
            'username': self.username
        })
        self.assertContains(response, 'Both username and password are required.')

    def test_ajax_login_successful(self):
        """Test successful login via AJAX."""
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Login successful'})

    def test_ajax_login_failure(self):
        """Test failed login via AJAX."""
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

class RegistrationViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_registration_success(self):
        """Test if a new user can successfully register."""
        form_data = {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'newuser@example.com'
        }
        response = self.client.post(self.register_url, data=form_data)
        self.assertRedirects(response, self.login_url)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertTrue(Profile.objects.filter(user__username='newuser').exists())

    def test_registration_invalid_form(self):
        """Test registration with invalid form data."""
        form_data = {
            'username': '',  # Invalid username
            'password1': 'password123',
            'password2': 'password123',
            'email': 'invalid-email'  # Invalid email
        }
        response = self.client.post(self.register_url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_ajax_registration_success(self):
        """Test successful registration via AJAX."""
        form_data = {
            'username': 'ajaxuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'ajaxuser@example.com'
        }
        response = self.client.post(self.register_url, data=form_data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'message': 'Account created for ajaxuser!'})
        self.assertTrue(User.objects.filter(username='ajaxuser').exists())
        self.assertTrue(Profile.objects.filter(user__username='ajaxuser').exists())

    def test_ajax_registration_failure(self):
        """Test registration failure via AJAX."""
        form_data = {
            'username': '',  # Missing username
            'password1': 'password123',
            'password2': 'password123',
            'email': 'invalid-email'  # Invalid email
        }
        response = self.client.post(self.register_url, data=form_data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.json())
        self.assertIn('username', response.json()['form'])
        self.assertIn('email', response.json()['form'])
