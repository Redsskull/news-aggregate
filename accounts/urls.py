from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomRegistrationView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
]