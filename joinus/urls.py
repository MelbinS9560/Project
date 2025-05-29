"""
URL configuration for joinus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.template.response import TemplateResponse

# Import models from all 3 apps
from payment.models import Donation as PaymentDonation
from excess.models import ExcessFood
from Registration.models import Donation as EssentialsDonation

# Custom admin index view
def custom_admin_index(request):
    from django.contrib.admin.sites import site

    context = dict(
        site.each_context(request),
        pending_payment_donations=PaymentDonation.objects.filter(status='Pending').order_by('-donation_date')[:5],
        pending_excess_donations=ExcessFood.objects.filter(status='Pending').order_by('-pickup_datetime')[:5],
        pending_essentials_donations=EssentialsDonation.objects.filter(status='Pending').order_by('-pickup_datetime')[:5],
    )
    return TemplateResponse(request, "admin/custom_index.html", context)

# Override default admin index
admin.site.index = custom_admin_index

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('about/', include('About.urls')),
    path('donation/', include('donation.urls')),
    path('excess/', include('excess.urls')),
    path('feedback/', include('feedback.urls')),
    path('history/', include('history.urls')),
    path('login/', include('login.urls')),
    path('payment/', include('payment.urls')),
    path('registration/', include('Registration.urls')),
]
