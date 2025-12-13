from django.contrib import admin
from home.models import Hero, HeroBadge
# Register your models here.

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ["title", "sub_title", "is_active", "created_at"]
    list_filter = ["is_active"]
    search_fields = ["title", "sub_title"]
    ordering = ["created_at"]


@admin.register(HeroBadge)
class HeroBadgeAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "created_by"]
    list_filter = ["created_by"]
    search_fields = ["title"]