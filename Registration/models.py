from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    condition = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    address = models.TextField()
    pickup_datetime = models.DateTimeField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
