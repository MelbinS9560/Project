from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Donation

@login_required
def register(request):
    if request.method == 'POST':
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
            message=request.POST.get('message'),
            donor=request.user  # assuming your Donation model has donor field as ForeignKey to User
        )
        messages.success(request, 'Thank you! Your donation has been recorded successfully!')
        return render(request, 'registration_page.html')

    return render(request, 'registration_page.html')

@login_required
def donation_data(request):
    donations = Donation.objects.all()
    context = {
        'donations': donations
    }
    return render(request, 'donation_data.html', context)
