from django.contrib import admin
from .models import (
    PopUp,
    MenuItem,
    MenuContent,
    Hero,
    HeroBadge,
    About,
    Health_package,
    Badge,
    AppointmentHomeImage,
    HomeService,
    CorporateCarousel,
)
from import_export.admin import ImportExportModelAdmin


@admin.register(PopUp)
class PopUpAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image"]
    search_fields = ["title"]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "our_mission_title",
        "our_vision_title",
        "video_link",
    ]
    list_filter = ["title", "our_mission_title", "our_vision_title"]
    search_fields = ["title", "our_mission_title", "our_vision_title"]


@admin.register(Health_package)
class Health_packageAdmin(admin.ModelAdmin):
    list_display = ["title", "gender", "price"]
    list_filter = ["gender", "price"]
    search_fields = ["title", "gender", "price"]


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = [
        "total_appointment",
        "specialists",
        "happy_patients",
        "winning_awards",
        "updated_at",
    ]
    search_fields = [
        "total_appointment",
        "specialists",
        "happy_patients",
        "winning_awards",
    ]


# @admin.register(Facilities)
# class FacilitiesAdmin(admin.ModelAdmin):
#     list_display = ['title', 'description', 'points', 'image', 'open_hour', 'created_at']
#     list_filter = ['created_at', 'open_hour']
#     search_fields = ['title', 'description', 'points']


@admin.register(AppointmentHomeImage)
class AppointmentHomeImageAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "created_at"]
    list_filter = ["is_active"]
    search_fields = ["title"]
    ordering = ["created_at"]


@admin.register(HomeService)
class HomeServiceAdmin(admin.ModelAdmin):
    list_display = ["service_title", "service_description"]
    list_filter = ["service_title"]
    search_fields = ["service_title", "service_description"]

@admin.register(CorporateCarousel)
class CorporateCarouselAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "created_at"]