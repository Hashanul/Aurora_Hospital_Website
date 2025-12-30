from django.contrib import admin
from .models import DepartmentBanner, DoctorBanner, Department, Doctor, DepartmentGroup
from import_export.admin import ImportExportModelAdmin
from .resources import DoctorResource, DepartmentResource


@admin.register(DepartmentBanner)
class DepartmentBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']


@admin.register(DoctorBanner)
class DoctorBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']



@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource
    list_display = ['id', 'name', 'description']
    search_fields = ['name', 'slug', 'description'] 


@admin.register(Doctor)
class DoctorAdmin(ImportExportModelAdmin):
    resource_class = DoctorResource
    list_display = ['id', 'drName', 'designation', 'department', 'drCode']
    list_filter = ['designation', 'department']
    search_fields = ['drName', 'designation']

@admin.register(DepartmentGroup)
class DepartmentGroupAdmin(admin.ModelAdmin):
    list_display = ['group_name']
    search_fields = ['group_name']




