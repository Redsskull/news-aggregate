from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'approved')


admin.site.register(Testimonial, TestimonialAdmin)


