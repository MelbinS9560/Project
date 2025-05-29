from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .models import ExcessFood


@login_required
def excess_food_view(request):
    if request.method == 'POST':
        # Directly create from POST data
        ExcessFood.objects.create(
            full_name=request.POST.get('full_name'),
            contact_number=request.POST.get('contact_number'),
            email=request.POST.get('email', ''),  # optional field
            food_type=request.POST.get('food_type'),
            cuisine_type=request.POST.get('cuisine_type'),
            servings=request.POST.get('servings'),
            best_before=request.POST.get('best_before'),
            pickup_address=request.POST.get('pickup_address'),
            pickup_datetime=request.POST.get('pickup_datetime'),
            additional_notes=request.POST.get('additional_notes', ''),
            donor=request.user
        )
        messages.success(request, 'Thank you! Your food donation has been recorded successfully!')

    return render(request, 'excess_page.html')
