from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active")  # Add fields you want to see
    search_fields = ("username", "email")  # Enable search by username & email
    list_filter = ("is_staff", "is_active")  # Add filters in admin panel

admin.site.register(CustomUser, CustomUserAdmin)
