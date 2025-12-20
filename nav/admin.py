from django.contrib import admin
from home.models import MenuItem, MenuContent
from import_export.admin import ImportExportModelAdmin


@admin.register(MenuItem)
class MenuItemAdmin(ImportExportModelAdmin):
    list_display = ["id", "title", "to", "classChange", "order"]
    search_fields = ["title"]


@admin.register(MenuContent)
class MenuContentAdmin(ImportExportModelAdmin):
    list_display = ["id", "title", "to", "menu"]
    search_fields = ["title"]
