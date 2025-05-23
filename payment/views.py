from django.shortcuts import render
from .models import Donation
from decimal import Decimal
from django.core.exceptions import ValidationError

def payment(request):
    if request.method == 'POST':
        donor_name = request.POST.get('donor_name')
        donor_account_no = request.POST.get('donor_account_no')
        amount = request.POST.get('donation_amount')
        submit_value = request.POST.get('submit', '')

        payment_method = 'online' if 'I have Paid' in submit_value else 'bank'

        donation = Donation(
            donor_name=donor_name,
            donor_account_no=donor_account_no,
            amount=Decimal(amount),
            payment_method=payment_method
        )

        try:
            donation.full_clean()  # This triggers model validators
            donation.save()
            return render(request, 'paymentpage.html', {'success': True})
        except ValidationError as e:
            return render(request, 'paymentpage.html', {
                'errors': e.message_dict,
                'donor_name': donor_name,
                'donor_account_no': donor_account_no,
                'amount': amount,
                'payment_method': payment_method,  # ✅ Ensures correct form is shown
            })

    return render(request, 'paymentpage.html')
