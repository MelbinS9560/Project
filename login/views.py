from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser

# Sign-Up View
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required!")
            return redirect("login_page")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("login_page")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("login_page")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("login_page")

        # Create user and save it
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully! Please sign in.")
        return redirect("login_page")  # Redirects to login page

    return render(request, "login.html")

# Sign-In View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #messages.success(request, "Login successful!")
            return redirect("Donation")  # Change to your actual homepage URL
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, "login.html")  # No need to pass error in context

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login_page")
