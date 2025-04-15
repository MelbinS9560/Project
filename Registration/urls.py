from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='registering_page'),       # Form page
    path('donation-data', views.donation_data, name='donation_data') # Admin/table page
]
