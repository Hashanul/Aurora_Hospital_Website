from django.contrib import admin
from .models import AppointmentBanner, Appointment


@admin.register(AppointmentBanner)
class AppointmentBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'created_by']



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['VisitDate', 'DrCode', 'DrName', 'PatientName', 'MobileNo', 'PatientEmail', 'Dob', 'AgeDay', 'AgeMonth', 'AgeYear', 'Sex', 'VisitAmount', 'VisitType']
    list_filter = ['VisitDate', 'DrCode', 'DrName', 'MobileNo']
    search_fields = ['PatientName', 'MobileNo', 'DrCode', 'DrName']



