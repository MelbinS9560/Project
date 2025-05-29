from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from payment.models import Donation as MoneyDonation
from excess.models import ExcessFood
from Registration.models import Donation as EssentialsDonation

@login_required
def my_donation_history(request):
    user = request.user

    # Use correct field names for ordering by date fields
    money_donations = MoneyDonation.objects.filter(donor=user).order_by('-donation_date')
    food_donations = ExcessFood.objects.filter(donor=user).order_by('-submitted_at')
    essentials_donations = EssentialsDonation.objects.filter(donor=user).order_by('-pickup_datetime')


    context = {
        'money_donations': money_donations,
        'food_donations': food_donations,
        'essentials_donations': essentials_donations,
    }

    return render(request, 'history/my_history.html', context)
    
