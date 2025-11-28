from django.contrib import admin
from .models import Hero, Badge, Facilities, Banner, ContactHome, MenuItem, MenuContent


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'to', 'classChange']

@admin.register(MenuContent)
class MenuContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'to']

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title']
    ordering = ['created_at']

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['total_appointment', 'specialists', 'happy_patients', 'winning_awards', 'updated_at']


@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'points', 'image', 'open_hour', 'created_at']
    list_filter = ['created_at', 'open_hour']
    search_fields = ['title', 'description', 'points']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title']
    ordering = ['created_at']

@admin.register(ContactHome)
class ContactHomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'created_at']
    list_filter = ['subject']
    search_fields = ['name', 'phone', 'email' 'subject']
    ordering = ['created_at']

