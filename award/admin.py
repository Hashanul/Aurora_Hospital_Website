from django.contrib import admin
from .models import AwardBanner, Award

# Register your models here.

@admin.register(AwardBanner)
class AwardBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'year', 'image', 'created_by']
    list_filter = ['title', 'year']
    search_fields = ['title', 'year']