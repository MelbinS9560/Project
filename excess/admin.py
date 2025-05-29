from django.contrib import admin
from .models import ExcessFood

@admin.register(ExcessFood)
class ExcessFoodAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'contact_number', 'food_type', 'cuisine_type', 'servings', 'pickup_datetime', 'status')
    list_filter = ('status', 'food_type', 'pickup_datetime')
    list_editable = ('status',)  # Enables admin to change status from list view
    search_fields = ('full_name', 'contact_number', 'email', 'food_type')
