from django.urls import path
from .views import TestimonialListView, AddTestimonialView,EditTestimonialView, DeleteTestimonialView

app_name = 'testimonials' 

urlpatterns = [
    path('', TestimonialListView.as_view(), name='testimonials_list'),  
    path('add/', AddTestimonialView.as_view(), name='add_testimonial'),
    path('<int:testimonial_id>/edit/', EditTestimonialView.as_view(), name='edit_testimonial'),
    path('<int:testimonial_id>/delete/', DeleteTestimonialView.as_view(), name='delete_testimonial'),  
]
