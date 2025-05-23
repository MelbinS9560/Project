from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class Donation(models.Model):
    name_validator = RegexValidator(regex=r'^[a-zA-Z\s]+$', message='Name should contain only letters and spaces.')
    phone_validator = RegexValidator(regex=r'^\d{10}$', message='Enter a valid 10-digit mobile number.')

    name = models.CharField(max_length=50, validators=[name_validator])
    mobile = models.CharField(max_length=10, validators=[phone_validator])
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    condition = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1, message="Quantity must be at least 1.")])
    address = models.TextField()
    pickup_datetime = models.DateTimeField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
