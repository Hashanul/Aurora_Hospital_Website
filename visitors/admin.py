from django.contrib import admin
from .models import RoomRent, Equipment, FeedbackBanner, Feedback



@admin.register(RoomRent)
class RoomRentAdmin(admin.ModelAdmin):
    list_display = ['bed_name', 'charges', 'created_by']
    search_fields = ['bed_name', 'charges']
    list_filter = ['charges']


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
    patient_name = ['title', 'Contact_number', 'hn_number', 'email', 'consultant_name', 'created_by']
    search_fields = ['title', 'Contact_number', 'hn_number', 'consultant_name']
    list_filter = ['consultant_name']
