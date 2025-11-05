from django.db import models
from django.contrib.auth.models import User

 

class Hero(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='media/hero/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hero Section: {self.title}"

class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='media/banner/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Banner Section: {self.title}"







