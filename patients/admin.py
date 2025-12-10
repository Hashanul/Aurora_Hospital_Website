from django.contrib import admin
from .models import Patient, PatientBanner


@admin.register(PatientBanner)
class PatientBanner(admin.ModelAdmin):
    list_display = ['title', 'image']
    search_fields = ['title']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'gender', 'email', 'phone', 'address']
    list_filter = ['age', 'gender']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'gender']
