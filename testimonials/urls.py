from django.urls import path
from .views import TestimonialListView, AddTestimonialView

app_name = 'testimonials' 

urlpatterns = [
    path('list/', TestimonialListView.as_view(), name='testimonials_list'),  # Corrected TestimonialListView
    path('leave/', AddTestimonialView.as_view(), name='testimonials_leave'),  # Corrected AddTestimonialView
    path('add/', AddTestimonialView.as_view(), name='add_testimonial'),  # Corrected AddTestimonialView
]
