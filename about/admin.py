from django.contrib import admin
from .models import AboutBanner, BOD, ChairmanMessage, MDMessage



@admin.register(AboutBanner)
class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']


@admin.register(BOD)
class BODAdmin(admin.ModelAdmin):
    list_display = ['bod_name', 'bod_designation', 'bod_image', 'created_by']
    search_fields = ['bod_name', 'bod_designation']
    list_filter = ['bod_designation']


@admin.register(ChairmanMessage)
class ChairmanMessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'richtext', 'image', 'created_by']
    search_fields = ['title', 'richtext']


@admin.register(MDMessage)
class MDMessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'richtext', 'image', 'created_by']
    search_fields = ['title', 'richtext']

