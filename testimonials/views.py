from django.shortcuts import render, redirect
from django.views import View
from .models import Testimonial
from .forms import TestimonialForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages


class TestimonialListView(View):
    template_name = 'testimonials_list.html'

    def get(self, request):
        testimonials = Testimonial.objects.filter(approved=False)
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


class EditTestimonialView(View):
    template_name = 'edit_testimonial.html'

    def get(self, request, testimonial_id):
        testimonial = get_object_or_404(Testimonial, id=testimonial_id, user=request.user)
        form = TestimonialForm(instance=testimonial)
        return render(request, self.template_name, {'form': form, 'testimonial': testimonial})

    def post(self, request, testimonial_id):
        testimonial = get_object_or_404(Testimonial, id=testimonial_id, user=request.user)
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial updated successfully.')
            return redirect('testimonials:testimonials_list')
        return render(request, self.template_name, {'form': form, 'testimonial': testimonial})

class DeleteTestimonialView(View):
    template_name = 'delete_testimonial.html'

    def get(self, request, testimonial_id):
        testimonial = get_object_or_404(Testimonial, id=testimonial_id, user=request.user)
        return render(request, self.template_name, {'testimonial': testimonial})

    def post(self, request, testimonial_id):
        testimonial = get_object_or_404(Testimonial, id=testimonial_id, user=request.user)
        testimonial.delete()
        messages.success(request, 'Testimonial deleted successfully.')
        return redirect('testimonials:testimonials_list')


