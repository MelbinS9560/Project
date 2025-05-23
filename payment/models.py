from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class Donation(models.Model):
    PAYMENT_METHODS = [
        ('online', 'Online Transfer'),
        ('bank', 'Bank Transfer'),
    ]

    name_validator = RegexValidator(regex=r'^[a-zA-Z\s]+$', message='Name should contain only letters and spaces.')
    account_validator = RegexValidator(regex=r'^\d{8,20}$', message='Account number should be 8 to 20 digits.')

    donor_name = models.CharField(max_length=100, validators=[name_validator])
    donor_account_no = models.CharField(max_length=20, blank=True, null=True, validators=[account_validator])
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(10.00, message="Amount must be at least ₹10.")]
    )
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    donation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor_name} - ₹{self.amount} ({self.payment_method})"
