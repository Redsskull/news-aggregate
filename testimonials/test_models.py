from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Testimonial

class TestimonialModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='12345')
        Testimonial.objects.create(content='This is a test testimonial', user=user)

    def test_content_label(self):
        testimonial = Testimonial.objects.get(id=1)
        field_label = testimonial._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')


    def test_object_name_is_content(self):
        testimonial = Testimonial.objects.get(id=1)
        expected_object_name = f'{testimonial.user.username} - {testimonial.content[:20]}'
        self.assertEqual(expected_object_name, str(testimonial))