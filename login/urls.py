from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_view, name="login_page"),  # Sign In
    path("signup", views.signup_view, name="signup_page"),  # Sign Up
]
