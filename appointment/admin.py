
from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'department_name', 'doctor_name', 'schedule']
    list_filter = ['department_name', 'doctor_name', 'schedule']
    search_fields = ['patient_name', 'department_name', 'doctor_name']



