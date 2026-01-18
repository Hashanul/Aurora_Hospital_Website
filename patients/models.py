from django.db import models
from accounts.models import User
from doctors.models import Doctor, Department
from django_ckeditor_5.fields import CKEditor5Field


class PatientBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='patient_banner/', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title
    


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PatientStoryBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='patient-stories_banner/', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title
   

class PatientStory(models.Model):
    title = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=100)
    city = models.CharField(max_length=180, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    departmenmt = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    video_url = models.URLField(max_length=500, blank=True, null=True, help_text="Enter YouTube video URL")
    thumbnail = models.FileField(upload_to='patient_storie_thumbnail/', blank=True, null=True)
    description =  CKEditor5Field(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    
    def save(self, *args, **kwargs):
        """
        Auto set department from doctor
        Works for API + Admin + everywhere
        """
        if self.doctor:
            self.departmenmt = self.doctor.department
        else:
            self.departmenmt = None

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title if self.title else self.id} - Patient Name : {self.patient_name if self.patient_name else self.id}"


