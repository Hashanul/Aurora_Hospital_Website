from django.contrib import admin
from .models import AppointmentBanner, Appointment, Report


@admin.register(AppointmentBanner)
class AppointmentBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'created_by']
    search_fields = ['title']



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['VisitDate', 'DrCode', 'DrName', 'PatientName', 'MobileNo', 'PatientEmail', 'Dob', 'AgeDay', 'AgeMonth', 'AgeYear', 'Sex', 'VisitAmount', 'VisitType']
    list_filter = ['VisitDate', 'DrCode', 'DrName', 'MobileNo']
    search_fields = ['VisitDate', 'DrCode', 'DrName', 'PatientName', 'MobileNo', 'PatientEmail', 'Dob', 'Sex',]


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display= ['id', 'patient_id', 'report_file']
    list_filter= ['patient_id']
    search_fields = ['patient_id']
