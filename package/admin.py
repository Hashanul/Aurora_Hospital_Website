from django.contrib import admin
from .models import HealthPackageBanner, Health_package, Health_Service





@admin.register(HealthPackageBanner)
class HealthPackageBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']


@admin.register(Health_package)
class Health_packageAdmin(admin.ModelAdmin):
    list_display = ['title', 'gender', 'price']
    list_filter = ['gender', 'price']
    search_fields = ['title', 'gender', 'price']

@admin.register(Health_Service)
class Health_ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    search_fields = ['title']

