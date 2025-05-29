from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from payment.models import Donation as PaymentDonation
from excess.models import ExcessFood
from Registration.models import Donation as EssentialsDonation


class CustomAdminSite(admin.AdminSite):
    site_header = "Donation Admin Panel"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_view(self.custom_index), name="index"),
        ]
        return custom_urls + urls

    def custom_index(self, request):
        pending_payment_donations = PaymentDonation.objects.filter(status='Pending').order_by('-donation_date')[:5]
        pending_excess_donations = ExcessFood.objects.filter(status='Pending').order_by('-pickup_datetime')[:5]
        pending_essentials_donations = EssentialsDonation.objects.filter(status='Pending').order_by('-pickup_datetime')[:5]

        context = dict(
            self.each_context(request),
            pending_payment_donations=pending_payment_donations,
            pending_excess_donations=pending_excess_donations,
            pending_essentials_donations=pending_essentials_donations,
        )
        return TemplateResponse(request, "admin/custom_index.html", context)


# Replace default admin with this
custom_admin_site = CustomAdminSite(name='custom_admin')

# Register your models again here for custom site
from payment.models import Donation as PaymentDonation
from excess.models import ExcessFood
from Registration.models import Donation as EssentialsDonation

custom_admin_site.register(PaymentDonation)
custom_admin_site.register(ExcessFood)
custom_admin_site.register(EssentialsDonation)
