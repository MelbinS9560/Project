from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback  # Import model

def feedback_page(request):
    return render(request, 'feedbackpage.html')

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        message = request.POST.get('message')

        # Save feedback to the database
        Feedback.objects.create(name=name, rating=rating, message=message)

        messages.success(request, "Thank you for your feedback!")
        return redirect('homepage')

    return redirect('homepage')
