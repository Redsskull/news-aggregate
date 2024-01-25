from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'is_suspended', 'is_staff', 'is_superuser'
    )
    list_filter = ('is_suspended', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    actions = ['suspend_users', 'activate_users']

    def suspend_users(self, request, queryset):
        queryset.update(is_suspended=True)
    suspend_users.short_description = "Suspend selected users"

    def activate_users(self, request, queryset):
        queryset.update(is_suspended=False)
    activate_users.short_description = "Activate selected users"


admin.site.register(User, UserAdmin)
