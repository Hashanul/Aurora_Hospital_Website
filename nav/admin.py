from django.contrib import admin
from home.models import MenuItem, MenuContent
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

class MenuItemResource(resources.ModelResource):
    class Meta:
        model = MenuItem
        import_id_fields = ('title',)  # Use title as the unique identifier for matching
        skip_unchanged = True          # Skip rows if no changes detected
        report_skipped = True          # Report skipped duplicates in admin results
        fields = ('title', 'to', 'classChange', 'order')
        # Optionally exclude 'id' if you do not want to import/export it
        exclude = ('id',)

class MenuContentResource(resources.ModelResource):
    menu_title = fields.Field(
        column_name='menu',                    # Matches the exported column header 'menu'
        attribute='menu',
        widget=ForeignKeyWidget(MenuItem, field='title')
    )

    class Meta:
        model = MenuContent
        import_id_fields = ('title', 'menu_title')  # Use the custom field in import_id_fields
        skip_unchanged = True
        report_skipped = True
        fields = ('title', 'to', 'menu_title')      # Include menu_title explicitly
        exclude = ('id', 'menu')
        
@admin.register(MenuItem)
class MenuItemAdmin(ImportExportModelAdmin):
    resource_class = MenuItemResource
    list_display = ["id", "title", "to", "classChange", "order"]
    search_fields = ["title"]


@admin.register(MenuContent)
class MenuContentAdmin(ImportExportModelAdmin):
    resource_class = MenuContentResource
    list_display = ["id", "title", "to", "menu", "order"]
    search_fields = ["title"]

    readonly_fields = ['to']
 