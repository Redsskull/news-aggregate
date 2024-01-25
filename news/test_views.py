from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class HomePageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_page_url = reverse('home_page')

    @patch('requests.get')
    def test_home_page_view(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {
            'data': [
                {
                    'title': 'Test News',
                    'description': 'This is a test news article',
                    'image': 'http://example.com/image.jpg',
                    'url': 'http://example.com/news',
                    'published_at': '2022-01-01T00:00:00Z',
                }
            ]
        }

        response = self.client.get(self.home_page_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('news_list', response.context)
        self.assertEqual(len(response.context['news_list']), 1)
        