# from django import forms
# from .models import Appointment
# from doctors.models import Doctor

# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if 'department_name' in self.data:
#             try:
#                 department_id = int(self.data.get('department_name'))
#                 self.fields['doctor_name'].queryset = Doctor.objects.filter(department_id=department_id)
#             except (ValueError, TypeError):
#                 pass  # invalid input; fallback to default
#         elif self.instance.pk:
#             # When editing existing Appointment, show only doctors in that department
#             self.fields['doctor_name'].queryset = Doctor.objects.filter(department=self.instance.department_name)
#         else:
#             # Default: no doctors
#             self.fields['doctor_name'].queryset = Doctor.objects.none()
