# doctor/resources.py

from import_export import resources, fields, widgets
from .models import Doctor, Department

class CustomForeignKeyWidget(widgets.ForeignKeyWidget):
    def __init__(self, model, field='pk', create_if_not_exists=False, **kwargs):
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
        exclude = ('id', 'slug')  # id auto generate, slug auto generate
        import_id_fields = ()

class DoctorResource(resources.ModelResource):
    department = fields.Field(
        attribute='department',
        column_name='department',
        widget=CustomForeignKeyWidget(Department, 'name', create_if_not_exists=True)
    )

    class Meta:
        model = Doctor
        exclude = ('id',)   # <-- id auto generate হবে
        import_id_fields = ()  # ignore id entirely
