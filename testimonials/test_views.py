from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Testimonial

class TestimonialViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', email='testuser@example.com', password='12345')
        self.testimonial = Testimonial.objects.create(content='This is a test testimonial', user=self.user)
        self.client.login(username='testuser', password='12345')

    def test_testimonial_list_view(self):
        response = self.client.get(reverse('testimonials:testimonials_list'))
        self.assertEqual(response.status_code, 200)

    def test_add_testimonial_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('testimonials:add_testimonial'))
        self.assertEqual(response.status_code, 200)

    def test_edit_testimonial_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('testimonials:edit_testimonial', args=[self.testimonial.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_testimonial_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('testimonials:delete_testimonial', args=[self.testimonial.id]))
        self.assertEqual(response.status_code, 200)