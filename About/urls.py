from django.contrib import admin
from django.urls import path,include
 
from django.conf import settings 
from . import views

urlpatterns = [
    path('about ',views.About,name='about_page')
] 
