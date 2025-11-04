from rest_framework import serializers
from .models import Doctor, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(write_only=True, required=False, allow_blank=True)
    department_description = serializers.CharField(write_only=True, required=False, allow_blank=True)
    department = serializers.StringRelatedField(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), 
        source='department', 
        write_only=True, 
        required=False, 
        allow_null=True
    )

    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'email', 'phone', 'designation', 'description',
            'department_id','department', 'department_name', 'department_description',
            'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        # Extract and remove department_name so it doesn't go to Doctor.objects.create
        department_name = validated_data.pop('department_name', None)
        department_description = validated_data.pop('department_description', None)
    

        if department_name:
            # Get or create department
            department, created = Department.objects.get_or_create(name=department_name)
            validated_data['department'] = department
        if department_description and department_name:
            department.description = department_description
            department.save()
        # Now safe to create Doctor without extra fields
        doctor = Doctor.objects.create(**validated_data)
        return doctor
    

