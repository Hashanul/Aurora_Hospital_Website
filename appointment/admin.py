from django.contrib import admin
from .models import AppointmentBanner, Appointment, Report, AppointmentPackageBanner, AppointmentPackage, AppointmentPackageHeader


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


@admin.register(AppointmentPackageBanner)
class AppointmentPackageBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(AppointmentPackageHeader)
class AppointmentPackageBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sub_title']


@admin.register(AppointmentPackage)
class AppointmentPackageAdmin(admin.ModelAdmin):
    list_display = ['id', 
                    'patient_name',
                    'date_of_birth', 
                    'gender', 
                    'contact_number', 
                    'email', 
                    'health_package', 
                    'appointment_date', 
                    'appointment_time']

