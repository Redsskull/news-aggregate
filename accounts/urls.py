from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomRegistrationView
from .views import suspend_user

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('suspend/<int:user_id>/', suspend_user, name='suspend_user'),
]

