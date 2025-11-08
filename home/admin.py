from django.contrib import admin
from .models import Hero, Banner, Contact


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'image', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title']
    ordering = ['created_at']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'image', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title']
    ordering = ['created_at']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'created_at']
    list_filter = ['subject']
    search_fields = ['name', 'phone', 'email' 'subject']
    ordering = ['created_at']

