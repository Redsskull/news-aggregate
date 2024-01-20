from django.test import TestCase
from django.utils import timezone
from .models import BugReport

class BugReportModelTest(TestCase):

    def test_bug_report_creation(self):
   
        BugReport.objects.create(
            title="Test Bug",
            description="This is a test bug report.",
            submitted_at=timezone.now()
        )
        self.assertEqual(BugReport.objects.count(), 1)

    def test_bug_report_attributes(self):
   
        bug_report = BugReport.objects.create(
            title="Test Bug",
            description="This is a test bug report.",
            submitted_at=timezone.now()
        )

        self.assertEqual(bug_report.title, "Test Bug")
        self.assertEqual(bug_report.description, "This is a test bug report.")
        self.assertTrue(bug_report.submitted_at)

    def test_bug_report_str_representation(self):
    
        bug_report = BugReport.objects.create(
            title="Test Bug",
            description="This is a test bug report.",
            submitted_at=timezone.now()
        )

        self.assertEqual(str(bug_report), "Test Bug - {}".format(bug_report.submitted_at))


