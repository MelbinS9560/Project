from django.db import models

class ExcessFood(models.Model):
    FOOD_TYPE_CHOICES = [
        ('Cooked', 'Cooked'),
        ('Packaged', 'Packaged'),
        ('Raw', 'Raw'),
    ]

    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    food_type = models.CharField(max_length=20, choices=FOOD_TYPE_CHOICES)
    cuisine_type = models.CharField(max_length=100)
    servings = models.PositiveIntegerField()
    best_before = models.DateTimeField()
    pickup_address = models.TextField()
    pickup_datetime = models.DateTimeField()
    additional_notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.food_type}"
