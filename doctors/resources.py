# doctor/resources.py

from import_export import resources, fields, widgets
from .models import Doctor, Department, DepartmentGroup, ChamberTime
from import_export.results import RowResult




class CustomForeignKeyWidget(widgets.ForeignKeyWidget):
    def __init__(self, model, field="pk", create_if_not_exists=False, **kwargs):
        super().__init__(model, field, **kwargs)
        self.create_if_not_exists = create_if_not_exists

    def clean(self, value, row=None, **kwargs):
        if not value:
            return None
        try:
            return super().clean(value, row, **kwargs)
        except self.model.DoesNotExist:
            if self.create_if_not_exists:
                # Create the object if it doesn't exist
                obj = self.model.objects.create(**{self.field: value})
                return obj
            else:
                raise


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        exclude = ("id", "slug")  # id auto generate, slug auto generate
        import_id_fields = ()



class DoctorResource(resources.ModelResource):
    department = fields.Field(
        attribute="department",
        column_name="Department",
        widget=CustomForeignKeyWidget(
            Department, "name", create_if_not_exists=True
        ),
    )

    drName = fields.Field(attribute="drName", column_name="DrName")
    drCode = fields.Field(attribute="drCode", column_name="DrCode")
    designation = fields.Field(attribute="designation", column_name="Degree")
    drStatus = fields.Field(attribute="drStatus", column_name="DrStatus")
    takeCom = fields.Field(attribute="takeCom", column_name="TakeCom")
    drType = fields.Field(attribute="drType", column_name="DrType")
    sms = fields.Field(attribute="sms", column_name="SMS")
    phone = fields.Field(attribute="phone", column_name="CellPhone")

    # 🔹 Import শুরু হওয়ার আগে DB + file duplicate prepare
    def before_import(self, dataset, **kwargs):
        self.db_drcodes = set(
            Doctor.objects.exclude(drCode__isnull=True)
            .values_list("drCode", flat=True)
        )
        self.file_drcodes = set()

    # 🔹 Empty string → None (integer safe)
    def before_import_row(self, row, **kwargs):
        for key, value in row.items():
            if value == "":
                row[key] = None

    # 🔹 Main duplicate logic
    def import_row(self, row, instance_loader, **kwargs):
        drcode = row.get("DrCode")

        # drCode নাই → skip
        if not drcode:
            r = RowResult()
            r.import_type = RowResult.IMPORT_TYPE_SKIP
            return r

        # 🔥 DB duplicate → skip (LIVE DB check)
        if Doctor.objects.filter(drCode=drcode).exists():
            r = RowResult()
            r.import_type = RowResult.IMPORT_TYPE_SKIP
            return r

        # Same file duplicate → skip
        if drcode in self.file_drcodes:
            r = RowResult()
            r.import_type = RowResult.IMPORT_TYPE_SKIP
            return r

        # First valid drCode
        self.file_drcodes.add(drcode)
        return super().import_row(row, instance_loader, **kwargs)

    class Meta:
        model = Doctor

        # ❌ import_id_fields deliberately removed
        skip_unchanged = True
        report_skipped = True

        fields = (
            "id",
            "drName",
            "designation",
            "description",
            "richtext",
            "image",
            "drCode",
            "department",
            "email",
            "phone",
            "is_doctor",
            "drStatus",
            "takeCom",
            "drType",
            "sms",
        )
        exclude = ("created_by", "created_at", "updated_at")


# ===========================
# Custom ManyToMany Widget
# ===========================
class DepartmentManyToManyWidget(widgets.ManyToManyWidget):
    """
    Handles ManyToMany import/export for Departments.
    """

    def __init__(self, model, field="name", separator=","):
        super().__init__(model, field=field, separator=separator)

    def clean(self, value, row=None, **kwargs):
        """
        Import time:
        "Cardiology, Neurology" -> [Department objects] (only existing ones)
        """
        if not value:
            return []

        department_names = [v.strip() for v in value.split(self.separator)]
        departments = []

        for name in department_names:
            try:
                obj = self.model.objects.get(**{self.field: name})
                departments.append(obj)
            except self.model.DoesNotExist:
                pass  # Skip if department doesn't exist

        return departments

    def render(self, value, obj=None):
        """
        Export time:
        [Department objs] -> "Cardiology, Neurology"
        """
        if not value or not value.exists():
            return ""
        return self.separator.join(getattr(dept, self.field) for dept in value.all())


# ===========================
# DepartmentGroup Resource
# ===========================
class DepartmentGroupResource(resources.ModelResource):
    group_name = fields.Field(
        attribute="group_name",
        column_name="group name",
    )

    departments = fields.Field(
        attribute="departments",
        column_name="departments",
        widget=DepartmentManyToManyWidget(
            Department,
            field="name",     # Department name field
            separator=","
        ),
    )

    class Meta:
        model = DepartmentGroup
        fields = ("group_name", "departments")
        export_order = ("group_name", "departments")
        exclude = ("id", "created_by", "created_at")

        import_id_fields = ("group_name",)
        skip_unchanged = True
        report_skipped = True

    def save_m2m(self, instance, row, **kwargs):
        """
        ✔ Existing group → UPDATE
        ✔ New group → CREATE
        ✔ departments ADD হবে, old থাকবে
        """
        departments = self.fields["departments"].clean(row)
        if departments:
            instance.departments.add(*departments)

#=================================================

# yourapp/resources.py
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import ChamberTime, Doctor


class ChamberTimeResource(resources.ModelResource):
    # drCode দিয়ে ম্যাচ করবে (Doctor মডেলের drCode ফিল্ড unique হতে হবে!)
    drCode = fields.Field(
        column_name='drCode',                    
        attribute='drCode',                      
        widget=ForeignKeyWidget(Doctor, 'drCode')  
    )

    class Meta:
        model = ChamberTime
 
        fields = (
            'drCode',
            'dayName',
            'visitType',
            'startTime',
            'finishTime',
        )
        
        export_order = (
            'drCode',
            'dayName',
            'visitType',
            'startTime',
            'finishTime',
        )
        

        import_id_fields = ('drCode', 'dayName')
        

    