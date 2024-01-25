from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Testimonial(models.Model):
    user = models.ForeignKey\
        (User, on_delete=models.CASCADE, default=1)  # Temporary default
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}'
