from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class PaymentDonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'amount', 'payment_method', 'donation_date', 'status')
    list_filter = ('payment_method', 'status')
    search_fields = ('donor_name',)
    list_editable = ('status',)  # Make 'status' editable from the list page

    fields = ('donor_name', 'donor_account_no', 'amount', 'payment_method', 'status', 'donation_date')
    readonly_fields = ('donation_date',)  # donation_date should not be editable
