from django.test import TestCase
from .forms import CustomUserCreationForm


class CustomUserCreationFormTest(TestCase):
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

    def test_form_save(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        if form.is_valid():
            user = form.save()
            self.assertEqual(user.username, 'testuser')
            self.assertEqual(user.name, 'Test User')
            self.assertEqual(user.email, 'testuser@example.com')
