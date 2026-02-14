from django.contrib import admin
from .models import DepartmentBanner, DoctorBanner, HomeDepartmentHeader, HomeDoctorHeader, Department, DoctorImage, Doctor, DepartmentGroup, ChamberTime
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from .resources import DoctorResource, DepartmentResource, DepartmentGroupResource, ChamberTimeResource


@admin.register(DepartmentBanner)
class DepartmentBannerAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "created_by"]
    search_fields = ["title"]

@admin.register(DoctorBanner)
class DoctorBannerAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "created_by"]
    search_fields = ["title"]

@admin.register(HomeDepartmentHeader)
class HomeDepartmentHeaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sub_title']


@admin.register(HomeDoctorHeader)
class HomeDoctorHeaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sub_title']


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource
    list_display = ["id", "name", "description", "order"]
    search_fields = ["name", "slug", "description"]

    def get_import_formats(self):
        return [base_formats.CSV, base_formats.XLS, base_formats.XLSX]

    def get_export_formats(self):
        return [base_formats.CSV, base_formats.XLS, base_formats.XLSX]


@admin.register(DoctorImage)
class DoctorImageAdmin(ImportExportModelAdmin):

    list_display=['id', 'dr_image', 'drCode']


@admin.register(Doctor)
class DoctorAdmin(ImportExportModelAdmin):
    resource_class = DoctorResource
    list_display = ["id", "drName", "designation", "department", "drCode", "order"]
    list_filter = ["designation", "department"]
    search_fields = ["drName", "designation"]
    ordering = ['order']
    readonly_fields = ['image']

    def get_import_formats(self):
        return [base_formats.CSV, base_formats.XLS, base_formats.XLSX]

    def get_export_formats(self):
        return [base_formats.CSV, base_formats.XLS, base_formats.XLSX]


@admin.register(ChamberTime)
class ChamberTimeAdmin(ImportExportModelAdmin):
    resource_class = ChamberTimeResource
    list_display = ["id", "drCode", "dayName",
                    "visitType", "startTime", "finishTime"]
    autocomplete_fields = ['drCode']


@admin.register(DepartmentGroup)
class DepartmentGroupAdmin(ImportExportModelAdmin):
    resource_class = DepartmentGroupResource
    list_display = ["group_name"]
    search_fields = ["group_name"]
    autocomplete_fields = ['departments']

