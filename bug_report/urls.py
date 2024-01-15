from django.urls import path
from .views import submit_bug_report, confirmation

app_name = 'bug_report'

urlpatterns = [
    path('submit/', submit_bug_report, name='submit'),
    path('confirmation/', confirmation, name='confirmation'),
]