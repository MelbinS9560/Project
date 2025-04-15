from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique

    def __str__(self):
        return self.username
