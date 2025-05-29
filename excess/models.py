from django.db import models
from django.conf import settings  

class ExcessFood(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    food_type = models.CharField(max_length=50)
    cuisine_type = models.CharField(max_length=100)
    servings = models.PositiveIntegerField()
    best_before = models.DateTimeField()
    pickup_address = models.TextField()
    pickup_datetime = models.DateTimeField()
    additional_notes = models.TextField(blank=True)
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.food_type} ({self.status})"
