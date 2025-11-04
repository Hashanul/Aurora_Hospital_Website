from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Doctor(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Foreign keys
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialty})"


