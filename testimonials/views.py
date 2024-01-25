from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm


class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'testimonials_list.html'
    context_object_name = 'testimonials'

    def get_queryset(self):
        return Testimonial.objects.all()


class AddTestimonialView(View):
    template_name = 'add_testimonial.html'

    def get(self, request):
        form = TestimonialForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials:testimonials_list')
        return render(request, self.template_name, {'form': form})


class EditTestimonialView(View):
    template_name = 'edit_testimonial.html'

    def get(self, request, testimonial_id):
        testimonial = get_object_or_404(Testimonial, id=testimonial_id,
                                        user=request.user)
        form = TestimonialForm(instance=testimonial)
        return render(request, self.template_name,
                      {'form': form, 'testimonial': testimonial})

    def post(self, request, testimonial_id):
        testimonial = get_object_or_404(Testimonial, id=testimonial_id,
                                        user=request.user)
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.approved = False
            testimonial.save()
            return redirect('testimonials:testimonials_list')
        return render(request, self.template_name,
                      {'form': form, 'testimonial': testimonial})


class DeleteTestimonialView(View):
    def get(self, request, testimonial_id):
        testimonial = Testimonial.objects.filter(id=testimonial_id,
                                                 user=request.user)
        if testimonial:
            testimonial.delete()
            messages.success(request, 'Testimonial deleted successfully.')
        testimonials = Testimonial.objects.all()
        return render(request, 'testimonials_list.html',
                      {'testimonials': testimonials})
