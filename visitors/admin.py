from django.contrib import admin
from .models import VisitorPackage, PackageDetail, VisitorPackageBanner, FacilitiesBanner, EquipmentBanner, RoomRentBanner, RoomRent, VisitorService, Equipment, FeedbackBanner, Feedback, ServiceBanner
from import_export.admin import ImportExportModelAdmin
 

 
@admin.register(ServiceBanner)
class ServiceBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']

@admin.register(VisitorService)
class VisitorServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'richtext', 'created_by']
    search_fields = ['title']


@admin.register(FacilitiesBanner)
class FacilitiesBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']

@admin.register(VisitorPackageBanner)
class VisitorPackageBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']


@admin.register(VisitorPackage)
class VisitorPackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'urls']
    search_fields = ['title', 'urls'] 


@admin.register(PackageDetail)
class PackageDetailAdmin(ImportExportModelAdmin):
    list_display = ['package_title', 'procedure_name', 'package_duration', 'bed_category', 'package_rate', 'remarks']
    list_filter = ['package_title', 'package_duration', 'bed_category', 'package_rate', 'remarks']
    search_fields = ['package_title', 'procedure_name', 'bed_category']


@admin.register(RoomRentBanner)
class RoomRentBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']


@admin.register(RoomRent)
class RoomRentAdmin(ImportExportModelAdmin):
    list_display = ['bed_name', 'charges', 'created_by']
    list_filter = ['charges']
    search_fields = ['bed_name', 'charges']

@admin.register(EquipmentBanner)
class EquipmentBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'richtext', 'created_by']
    search_fields = ['title', 'richtext']

@admin.register(FeedbackBanner)
class FeedbackBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    patient_name = ['patient_name', 'Contact_number', 'hn_number', 'email', 'consultant_name', 'created_by']
    search_fields = ['patient_name', 'Contact_number', 'hn_number', 'consultant_name']
    list_filter = ['patient_name', 'consultant_name']
