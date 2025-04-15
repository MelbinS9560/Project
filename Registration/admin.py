from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'mobile',
        'category',
        'subcategory',
        'size',
        'gender',
        'condition',
        'quantity',
        'pickup_datetime',
    )
    search_fields = ('name', 'category', 'mobile')
    list_filter = ('category', 'condition', 'gender')
