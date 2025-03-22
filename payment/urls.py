
from django.contrib import admin
from django.urls import path,include
 
from django.conf import settings 
from . import views

urlpatterns = [
    path('Payment',views.payment,name='payment_page')
] 
