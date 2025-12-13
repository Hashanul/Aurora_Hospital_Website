from django.db import models
from accounts.models import User 
from PIL import Image
from django.core.exceptions import ValidationError
from accounts.models import User
from doctors.models import Department
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field




class PopUp(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='popup_image/', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    to = models.CharField(max_length=255, blank=True, null=True)
    classChange = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.to:
            self.to = "/" + slugify(self.title)
        super().save(*args, **kwargs)

 
    def __str__(self):
        return self.title


class MenuContent(models.Model):
    menu = models.ForeignKey(
        MenuItem,
        related_name="content",
        on_delete=models.CASCADE
    ) 

    # these appear INSIDE content[] array
    title = models.CharField(max_length=255)
    to = models.CharField(max_length=255, blank=True, null=True)
    # type = models.CharField(max_length=255, choices=TYPE_CHOICE, null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.to:
            # Example output: "Main-Menu/about-us"
            self.to = f"/{slugify(self.menu.title)}/{slugify(self.title)}"
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Content: {self.title} → Menu:{self.menu.title}"



class Hero(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    pc_image = models.ImageField(upload_to='hero/', null=True, blank=True)
    tab_image = models.ImageField(upload_to='hero/', null=True, blank=True)
    mobile_image = models.ImageField(upload_to='hero/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.image:
    #         return    
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def __str__(self):
        return f"Hero Section: {self.title if self.title else self.id}"



def validate_image_file(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg']
    import os
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Allowed: {valid_extensions}')
    
class HeroBadge(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(
        upload_to='HeroBadge/',
        blank=True,
        null=True,
        validators=[validate_image_file])
    url = models.CharField(max_length=255, null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else self.id



class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    our_mission_title = models.CharField(max_length=255, blank=True, null=True)
    our_mission_description = CKEditor5Field(blank=True, null=True)
    our_vision_title = models.CharField(max_length=255, blank=True, null=True)
    our_vision_description = CKEditor5Field(blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"




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
  



class Badge(models.Model):
    total_appointment = models.PositiveIntegerField(default=0)
    specialists = models.PositiveIntegerField(default=0)
    happy_patients = models.PositiveIntegerField(default=0)
    winning_awards = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Badge"
     

class Facilities(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    # Points of facility (store multiple lines separated by comma)
    points = models.TextField(null=True, blank=True, help_text="Write each point separated by a comma")
    
    image = models.ImageField(upload_to='facilities', blank=True, null=True)
    open_hour = models.TextField(null=True, blank=True, help_text="Write hours separated by comma, e.g., Saturday 6:00 am - 10:00 pm, Sunday 6:00 am - 10:00 pm")

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_points_list(self):
        """Return list of points (split by comma)."""
        if self.points:
            return [p.strip() for p in self.points.split(',')]
        return []

    def get_open_hours_list(self):
        """Return list of open hours (split by comma)."""
        if self.open_hour:
            return [h.strip() for h in self.open_hour.split(',')]
        return []


    def __str__(self):
        return f"Facilities : {self.title}"



class AppointmentHomeImage(models.Model):
    title = models.CharField(max_length=255)
    pc_image = models.ImageField(upload_to='appointment_Home_image/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.image:
    #         return
        
    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def __str__(self):
        return f"Appointment Home Image Section: {self.title}"
    



class HomeService(models.Model):
    service_title = models.CharField(max_length=255)
    service_category = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)
    service_image = models.FileField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service Title: {self.service_title}"