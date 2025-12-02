from django.contrib import admin
from .models import AboutBanner, BOD, ChairmanMessage, MDMessage



@admin.register(AboutBanner)
class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']




@admin.register(BOD)
class BODAdmin(admin.ModelAdmin):
    list_display = ['id', 'bod_drName', 'bod_name', 'bod_designation']

@admin.register(ChairmanMessage)
class ChairmanMessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'richtext', 'image', 'created_by']
    search_fields = ['title', 'richtext']


@admin.register(MDMessage)
class MDMessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'richtext', 'image', 'created_by']
    search_fields = ['title', 'richtext']

