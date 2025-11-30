from django.db import models
from accounts.models import User





class RoomRent(models.Model):
    bed_name = models.CharField(max_length=200)
    charges = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.bed_name


class FeedbackBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='feedback/', null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback Banner : {self.title}"
    


class Feedback(models.Model):
    CHOICES =[
        ("Poor", "Poor"),
        ("Good", "Good"),
        ("Excellent", "Excellent"),
    ]

    patient_name = models.CharField(max_length=255)
    Contact_number = models.CharField(max_length=20)
    hn_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    ipd = models.BooleanField(default=False)
    opd = models.BooleanField(default=False)
    day_care = models.BooleanField(default=False)
    consultant_name = models.CharField(max_length=255, null=True, blank=True)

    Ambiance = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    CustomerCareService = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    Doctors_Service = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    Nurses_Service = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    PatientCareAttendantService = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    HousekeepingService = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    BillingService = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    CleaningService = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    FoodQuality = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)



