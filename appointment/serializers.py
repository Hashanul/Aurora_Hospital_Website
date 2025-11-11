# from rest_framework import serializers
# from .models import Appointment
# from doctors.models import Department, Doctor, Schedule

# class AppointmentSerializer(serializers.ModelSerializer):
#     department_name = serializers.PrimaryKeyRelatedField(
#         queryset=Department.objects.all()
#     )
#     doctor_name = serializers.PrimaryKeyRelatedField(
#         queryset=Doctor.objects.all()
#     )
#     schedule = serializers.PrimaryKeyRelatedField(
#         queryset=Schedule.objects.all()
#     )

#     class Meta:
#         model = Appointment
#         fields = '__all__'

#     def to_representation(self, instance):
        
#         representation = super().to_representation(instance)
#         representation['department_name'] = instance.department_name.name if instance.department_name else None
#         representation['doctor_name'] = str(instance.doctor_name) if instance.doctor_name else None
#         representation['schedule'] = str(instance.schedule) if instance.schedule else None
#         return representation


from rest_framework import serializers
from .models import Appointment
from doctors.models import Doctor

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Only filter if request context is provided
        request = self.context.get('request')  
        if request:
            # Get department_id from query params
            department_id = request.query_params.get('department_id')
            if department_id:
                self.fields['doctor_name'].queryset = Doctor.objects.filter(department_id=department_id)
            else:
                # If no department selected, hide doctors
                self.fields['doctor_name'].queryset = Doctor.objects.all()

