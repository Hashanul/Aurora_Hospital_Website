from django.db import models
from accounts.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Health_Check_upBanner(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='package_banner/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Health Package Banner : {self.title}"

class Health_Check_up(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="health_service/", null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Health_Check_up :{self.title}"

class ServiceBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='service_banner/', null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service Banner : {self.title}"
    
class VisitorService(models.Model):
    title = models.CharField(max_length=255)
    richtext = CKEditor5Field( blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" Visitor Service : {self.title}"
    
class FacilitiesBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='facilities_banner/', null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Facilities Banner : {self.title}"

class VisitorPackageBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='package_banner/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"VisitorPackageBanner : {self.title}"

class VisitorPackage(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='visitor_package/', null=True, blank=True)
    urls = models.CharField(max_length=255, blank=True, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Visitor Package : {self.title}"
    
class PackageDetail(models.Model):
    package_title = models.ForeignKey(VisitorPackage, on_delete=models.SET_NULL, null=True, blank=True)
    procedure_name = models.CharField(max_length=255)
    package_duration = models.CharField(max_length=20, null=True, blank=True)
    bed_category = models.CharField(max_length=100, null=True, blank=True)    
    package_rate = models.PositiveIntegerField(null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Package Detail : {self.procedure_name}"

class RoomRentBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='room_rent_banner/', null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room Rent Banner : {self.title}"

class RoomRent(models.Model):
    bed_name = models.CharField(max_length=200)
    charges = models.PositiveIntegerField(null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bed_name

class EquipmentBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='equipment_banner/', null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Equipment Banner : {self.title}"

class Equipment(models.Model):
    title = models.CharField(max_length=255)
    richtext = CKEditor5Field( blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class FeedbackBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='feedback_banner/', null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
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

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback : {self.patient_name}"

