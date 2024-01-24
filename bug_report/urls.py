from django.urls import path
from .views import submit_bug_report
from news.views import home_page

app_name = 'bug_report'

urlpatterns = [
    path('submit/', submit_bug_report, name='submit'),
    path('home_page/', home_page, name='home_page'),
]