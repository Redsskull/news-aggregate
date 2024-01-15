from django.shortcuts import render, redirect
from django.views import View
from .models import Testimonial
from .forms import TestimonialForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class TestimonialListView(View):
    template_name = 'testimonials_list.html'

    def get(self, request):
        testimonials = Testimonial.objects.filter(approved=True)
        return render(request, self.template_name, {'testimonials': testimonials})

class AddTestimonialView(View):
    template_name = 'add_testimonial.html'

    def get(self, request):
        form = TestimonialForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            # I will add a message here, or a redirect
            return redirect('testimonials:testimonials_list')
        return render(request, self.template_name, {'form': form})



