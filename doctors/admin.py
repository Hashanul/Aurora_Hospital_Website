from django.contrib import admin
from .models import Department, Doctor, Service, DepartmentGroup, Schedule

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'department']
    list_filter = ['designation', 'department']
    search_fields = ['name', 'designation']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'service_category', 'service_description']
    list_filter = [ 'service_category', 'service_description']
    search_fields = ['service_title']


@admin.register(DepartmentGroup)
class DepartmentGroupAdmin(admin.ModelAdmin):
    list_display = ['group_name']
    search_fields = ['group_name']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['day', 'time']

