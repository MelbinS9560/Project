from django.urls import path
from . import views

urlpatterns = [
    path('my-donations/', views.my_donation_history, name='my_donation_history'),
]
