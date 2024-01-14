from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]


# from django.urls import path
# from .views import NewsView

# app_name = 'news'

# urlpatterns = [
#     path('', NewsView.as_view(), name='index'),
#     # Other URL patterns for your news app
# ]
