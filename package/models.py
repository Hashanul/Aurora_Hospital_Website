from django.db import models
from accounts.models import User
from django_ckeditor_5.fields import CKEditor5Field



class HealthPackageBanner(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='package_banner/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Health Package Banner : {self.title}"


class Health_package(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Male & Female', 'Male & Female'),
        ('Other', 'Other'),
    ] 
    
    
    title = models.CharField(max_length=255)
    description = CKEditor5Field(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)   
    price = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=255, blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Health Package: {self.title} - {self.gender}"
  

class Health_Service(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="health_service/", null=True, blank=True)

    def __str__(self):
        return f"Health_Service :{self.title}"


