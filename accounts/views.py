from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect

# Custom Login View
class CustomLoginView(LoginView):
    """
    Custom Login View that extends Django's built-in LoginView.
    This view handles user login and redirects authenticated users.
    """
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        response = super().form_valid(form)
        return response

# Custom Logout View
class CustomLogoutView(LogoutView):
    """
    Custom Logout View that extends Django's built-in LogoutView.
    This view handles user logout and displays a success message.
    """
    template_name = 'logout.html'

    def dispatch(self, request, *args, **kwargs):
        """
        This method is called before the view function.
        It handles user logout and displays a success message.
        """
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Logout successful. Goodbye!')
        return response

# Custom Registration View
class CustomRegistrationView(CreateView):
    """
    Custom Registration View that extends Django's built-in CreateView.
    This view handles user registration and redirects to the login page upon successful registration.
    """
    model = User
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully. Please log in.')
        return response
    

@user_passes_test(lambda u: u.is_superuser)
def suspend_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_suspended = True
    user.save()
    return redirect('admin:accounts_customuser_changelist')