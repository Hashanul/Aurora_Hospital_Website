from django.db import models
from django.contrib.auth.models import User 


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.name


class Schedule(models.Model):
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Day: {self.day}, Time: {self.time}"


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Foreign keys
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.name} - ({self.department})"
    

class Service(models.Model):
    service_title = models.CharField(max_length=255)
    service_category = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service Title: {self.service_title}"
    

class DepartmentGroup(models.Model):
    group_name = models.CharField(max_length=250, null=True, blank=True)
    departments = models.ManyToManyField(Department, blank=True, related_name='groups')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.group_name} - {self.departments}" 
    

