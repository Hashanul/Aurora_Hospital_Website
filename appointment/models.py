from django.db import models



class Appointment(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=15)
    patient_email = models.EmailField(unique=True)
