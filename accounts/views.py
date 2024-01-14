from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

class CustomRegistrationView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('login')


