from django.test import TestCase, Client
from django.urls import reverse
from bug_report.models import BugReport

class SubmitBugReportViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.submit_bug_report_url = reverse('bug_report:submit')

    def test_submit_bug_report_view_POST_adds_new_bug_report(self):
        response = self.client.post(self.submit_bug_report_url, {
            'title': 'Test Bug',
            'description': 'This is a test bug report',
        })

        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertEqual(BugReport.objects.count(), 1)  # Check if a new bug report was added
        self.assertEqual(BugReport.objects.first().title, 'Test Bug')  # Check if the title of the new bug report is correct

    def test_submit_bug_report_view_GET(self):
        response = self.client.get(self.submit_bug_report_url)

        self.assertEqual(response.status_code, 200)  # Check if the page loads successfully
        self.assertTemplateUsed(response, 'submit_bug_report.html')  # Check if the correct template is used