from django.contrib import admin
from .models import Hero


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'image', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title']
    ordering = ['created_at']
