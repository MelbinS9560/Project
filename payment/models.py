from django.db import models

class Donation(models.Model):
    PAYMENT_METHODS = [
        ('online', 'Online Transfer'),
        ('bank', 'Bank Transfer'),
    ]

    donor_name = models.CharField(max_length=100)
    donor_account_no = models.CharField(max_length=20, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    donation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor_name} - ₹{self.amount} ({self.payment_method})"
