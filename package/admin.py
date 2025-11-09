from django.contrib import admin
from .models import Health_package


@admin.register(Health_package)
class Health_packageAdmin(admin.ModelAdmin):
    list_display = ['title', 'gender', 'price']
    list_filter = ['gender', 'price']
    search_fields = ['title']


