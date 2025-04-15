from django.shortcuts import render
from .models import Donation
from decimal import Decimal

def payment(request):
    print("🔔 Payment view triggered")  # Debug

    if request.method == 'POST':
        print(f"🔍 Form data received: {request.POST}")
        donor_name = request.POST.get('donor_name')
        donor_account_no = request.POST.get('donor_account_no')
        amount = request.POST.get('donation_amount')
        payment_method = 'online' if 'I have Paid' in request.POST.get('submit', '') else 'bank'

        print(f"🧾 Name: {donor_name}, Account: {donor_account_no}, Amount: {amount}, Method: {payment_method}")

        Donation.objects.create(
            donor_name=donor_name,
            donor_account_no=donor_account_no,
            amount=Decimal(amount),
            payment_method=payment_method
        )
        return render(request, 'paymentpage.html', {'success': True})

    return render(request, 'paymentpage.html')
