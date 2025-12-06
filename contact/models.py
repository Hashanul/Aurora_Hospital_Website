from django.db import models
from accounts.models import User
from doctors.models import Doctor



class ContactBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='contact_banner/', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"News Hero : {self.title}"
    


class ContactPage(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.TextField( null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # def total_doctor(self):
    #     return Doctor.objects.count()

    # @property
    # def doctor_images(self):
    #     return Doctor.objects.values_list('image', flat=True)
 


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contact Information: {self.name} - {self.subject}"
    

class Contact_data(models.Model):
    hotline= models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fb_link = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    youtub = models.CharField(max_length=255, null=True, blank=True)
    x_link = models.CharField(max_length=255, null=True, blank=True)
    instra_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Hotline {self.hotline}" 