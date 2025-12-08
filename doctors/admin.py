from django.contrib import admin
from .models import DepartmentBanner, DoctorBanner, Department, Doctor, ChamberTime, BestDoctor, DepartmentGroup


@admin.register(DepartmentBanner)
class DepartmentBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']


@admin.register(DoctorBanner)
class DoctorBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['title']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'drName', 'designation', 'department', 'drCode']
    list_filter = ['designation', 'department']
    search_fields = ['drName', 'designation']

@admin.register(ChamberTime)
class ChamberTimeAdmin(admin.ModelAdmin):
    list_display = ['drCode', 'dayName', 'visitType', 'startTime', 'finishTime', 'created_by']
    list_filter = ['drCode', 'dayName', 'visitType',]
    search_fields = ['drCode', 'dayName', 'visitType',]

@admin.register(BestDoctor)
class BestDoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'best_in_field', 'doctor_image', 'doctor_about', 'doctor_skills', 'doctor_experiance', 'award_title', 'award_description', 'award_image']
    list_filter = ['best_in_field', 'award_title', 'award_description', 'doctor_experiance',]
    search_fields = ['doctor_name', 'best_in_field', 'award_title',]





@admin.register(DepartmentGroup)
class DepartmentGroupAdmin(admin.ModelAdmin):
    list_display = ['group_name']
    search_fields = ['group_name']


# @admin.register(Schedule)
# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ['day', 'time']

