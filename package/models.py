from django.db import models
from accounts.models import User

class Health_package(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)   
    price = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=255, blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Health Package: {self.title} - {self.gender}"
  