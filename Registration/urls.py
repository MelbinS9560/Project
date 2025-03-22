
from django.contrib import admin
from django.urls import path,include
 
from django.conf import settings 
from . import views

urlpatterns = [
    path('register',views.register,name='registering_page')
] 
