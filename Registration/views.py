from django.shortcuts import render, redirect
from .models import Donation
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages  # ✅ For showing success messages

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # Save form data to model
        Donation.objects.create(
            name=request.POST.get('name'),
            mobile=request.POST.get('mobile'),
            category=request.POST.get('category'),
            subcategory=request.POST.get('subcategory') or '',
            size=request.POST.get('size') or '',
            gender=request.POST.get('gender') or '',
            condition=request.POST.get('condition'),
            quantity=request.POST.get('quantity'),
            address=request.POST.get('address'),
            pickup_datetime=request.POST.get('pickup'),
            message=request.POST.get('message')
        )
        messages.success(request, 'Thank you! Your donation has been recorded successfully!')
        return render(request, 'registration_page.html')  # ✅ Re-render same page with message

    return render(request, 'registration_page.html')

def donation_data(request):
    donations = Donation.objects.all()
    return redirect("Donation")  # ✅ You can adjust this as needed
