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
from django.urls import path,include
 
from django.conf import settings 
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path("",include('donation.urls')),
    path("",include('homepage.urls')),
    path("",include('About.urls')),
    path("",include('Registration.urls')),
    path("",include('payment.urls')),
    path("",include('excess.urls')),
    path("",include('login.urls')), 
    path('', include('donation.urls')),
    path('excess/', include('excess.urls')),

    
] 
 