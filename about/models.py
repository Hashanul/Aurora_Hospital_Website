from django.db import models
from accounts.models import User
from doctors.models import Doctor
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class AboutBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='about_banner/', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About Banner : {self.title}"


class BOD(models.Model):
    bod_drName =models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True )
    bod_name = models.CharField(max_length=255, null=True, blank=True)
    bod_designation = models.CharField(max_length=255)
    bod_image = models.FileField(upload_to='board_of_directors/', null=True, blank=True)
    bod_richtext = CKEditor5Field(blank=True, null=True)
  
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Board of Directors : {self.bod_name}"


class ChairmanMessage(models.Model):
    title = models.CharField(max_length=255)
    richtext = CKEditor5Field(blank=True, null=True)
    image = models.FileField(upload_to='chairman/', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message of Chairman : {self.title}"



class MDMessage(models.Model):
    title = models.CharField(max_length=255)
    richtext = CKEditor5Field(blank=True, null=True)
    image = models.FileField(upload_to='managing_director/', blank=True, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message of Managing Director : {self.title}"
