from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}⭐)"
