from django.db import models


class BugReport(models.Model):
    # a simple model to allow users to report a bug
    title = models.CharField(max_length=255)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.submitted_at}"
