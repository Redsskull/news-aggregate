from django.test import TestCase
from bug_report.forms import BugReportForm


class BugReportFormTest(TestCase):
    def test_form_has_fields(self):
        form = BugReportForm()
        expected = ['title', 'description']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

    def test_valid_form(self):
        data = {
            'title': 'Test Bug', 
            'description': 'This is a test bug report'
        }
        form = BugReportForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'title': '', 
            'description': 'This is a test bug report'
        }
        form = BugReportForm(data)
        self.assertFalse(form.is_valid())
        