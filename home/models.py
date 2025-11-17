from django.db import models
from django.conf import settings
from PIL import Image

 

class Hero(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    pc_image = models.ImageField(upload_to='media/hero/', null=True, blank=True)
    tab_image = models.ImageField(upload_to='media/hero/', null=True, blank=True)
    mobile_image = models.ImageField(upload_to='media/hero/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
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
        return f"Hero Section: {self.title}"



class Badge(models.Model):
    total_appointment = models.PositiveIntegerField(default=0)
    specialists = models.PositiveIntegerField(default=0)
    happy_patients = models.PositiveIntegerField(default=0)
    winning_awards = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Badge"
    
from django.db import models

class Facilities(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    # Points of facility (store multiple lines separated by comma)
    points = models.TextField(null=True, blank=True, help_text="Write each point separated by a comma")
    
    image = models.ImageField(upload_to='media/facilities', blank=True, null=True)
    open_hour = models.TextField(null=True, blank=True, help_text="Write hours separated by comma, e.g., Saturday 6:00 am - 10:00 pm, Sunday 6:00 am - 10:00 pm")
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
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



class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    pc_image = models.ImageField(upload_to='media/banner/', null=True, blank=True)
    tab_image = models.ImageField(upload_to='media/banner/', null=True, blank=True)
    mobile_image = models.ImageField(upload_to='media/banner/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.image:
            return
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"Banner Section: {self.title}"
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contact Information: {self.name} - {self.subject}"





