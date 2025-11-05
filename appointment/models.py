from django.db import models
from doctors.models import Department, Doctor, Schedule



class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=15)
    patient_email = models.EmailField(unique=True)
    department_name = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    doctor_name = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True, blank=True)
