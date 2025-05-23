from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxLengthValidator, EmailValidator

class ExcessFood(models.Model):
    FOOD_TYPE_CHOICES = [
        ('Cooked', 'Cooked'),
        ('Packaged', 'Packaged'),
        ('Raw', 'Raw'),
    ]

    name_validator = RegexValidator(regex=r'^[a-zA-Z\s]+$', message='Name should contain only letters and spaces.')
    phone_validator = RegexValidator(regex=r'^\d{10}$', message='Enter a valid 10-digit contact number.')

    full_name = models.CharField(max_length=100, validators=[name_validator])
    contact_number = models.CharField(max_length=10, validators=[phone_validator])
    email = models.EmailField(blank=True, validators=[EmailValidator(message="Enter a valid email address.")])
    
    food_type = models.CharField(max_length=20, choices=FOOD_TYPE_CHOICES)
    cuisine_type = models.CharField(max_length=100, validators=[name_validator])
    servings = models.PositiveIntegerField(validators=[MinValueValidator(1, message="Must be at least 1 serving.")])
    
    best_before = models.DateTimeField()
    pickup_address = models.TextField()
    pickup_datetime = models.DateTimeField()
    additional_notes = models.TextField(blank=True)
    
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.food_type}"
