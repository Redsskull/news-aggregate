from django.test import TestCase
from .forms import TestimonialForm
from django.contrib.auth import get_user_model


class TestimonialFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='12345'
        )

    def test_form_validity(self):
        form = TestimonialForm({
            'content': 'This is a test testimonial',
            'user': self.user.id
        })
        self.assertTrue(form.is_valid())

    def test_form_invalidity(self):
        form = TestimonialForm({})
        self.assertFalse(form.is_valid())
        