from django.contrib import admin
from .models import Patient, PatientBanner, PatientStory, PatientStoryBanner


# @admin.register(PatientBanner)
# class PatientBanner(admin.ModelAdmin):
#     list_display = ['title', 'image']
#     search_fields = ['title']

# @admin.register(Patient)
# class PatientAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'age', 'gender', 'email', 'phone', 'address']
#     list_filter = ['age', 'gender']
#     search_fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'gender']
  

@admin.register(PatientStoryBanner)
class PatientStoryBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    search_fields = ['title']

@admin.register(PatientStory)
class PatientStorieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'patient_name', 'city', 'doctor', 'department', 'video_url', 'thumbnail']
    list_filter = ['title', 'patient_name', 'city', 'doctor', 'department']
    search_fields = ['title', 'patient_name', 'city', 'doctor', 'department']

    readonly_fields = ['department', 'created_by']

    autocomplete_fields = ['doctor']

    def save_model(self, request, obj, form, change):
        """
        Auto set created_by in Django Admin
        """
        if not obj.pk:  # only on create
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

