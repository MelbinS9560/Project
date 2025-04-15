from django.contrib import admin
from .models import ExcessFood

@admin.register(ExcessFood)
class ExcessFoodAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'contact_number', 'food_type', 'cuisine_type', 'servings', 'pickup_datetime')
    search_fields = ('full_name', 'contact_number', 'email')
    list_filter = ('food_type', 'pickup_datetime')
