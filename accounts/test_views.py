from django.test import TestCase, Client
from django.urls import reverse
from accounts.views import (
    CustomLoginView, CustomLogoutView, CustomRegistrationView
)
from accounts.forms import CustomUserCreationForm
from accounts.models import User


class CustomLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')

    def test_login_template(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class CustomLogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse('logout')

    def test_logout_template(self):
        response = self.client.get(self.logout_url)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.status_code, 302)
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Logout successful. Goodbye!')


class CustomRegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_registration_template(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_form_valid(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'name': 'Test User',
            'email': '',  # Invalid email
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertFalse(form.is_valid())
