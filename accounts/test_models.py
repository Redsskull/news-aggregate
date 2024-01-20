from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class CustomUserManagerTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.check_password('foo'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_empty_email(self):
        User = get_user_model()
        with self.assertRaises(ValueError):
            User.objects.create_user(email=None, password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.check_password('foo'))
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        User.objects.create_user(email='test@user.com', password='foo', name='Test User')

    def test_email_label(self):
        User = get_user_model()
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_name_label(self):
        User = get_user_model()
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_object_name_is_email(self):
        User = get_user_model()
        user = User.objects.get(id=1)
        expected_object_name = user.email
        self.assertEqual(str(user), expected_object_name)

    def test_get_full_name(self):
        User = get_user_model()
        user = User.objects.get(id=1)
        self.assertEqual(user.get_full_name(), 'Test User')

    def test_get_short_name(self):
        User = get_user_model()
        user = User.objects.get(id=1)
        self.assertEqual(user.get_short_name(), 'Test User')