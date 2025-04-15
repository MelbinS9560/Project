from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ExcessFoodForm  # This is the form we created
from .models import ExcessFood     # This is your model

def excess_food_view(request):
    if request.method == 'POST':
        form = ExcessFoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your food donation has been recorded successfully.')
            return redirect('excess_page')  # Redirect back to the same page after submission
    else:
        form = ExcessFoodForm()
    
    return render(request, 'excess_page.html', {'form': form})
