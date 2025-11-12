from rest_framework import serializers
from .models import Doctor, Department, Schedule, Service, DepartmentGroup

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
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

    schedule_day = serializers.CharField(write_only=True, required=False, allow_blank=True)
    schedule_time = serializers.CharField(write_only=True, required=False, allow_blank=True)
    schedule = serializers.StringRelatedField(read_only=True)
    schedule_id = serializers.PrimaryKeyRelatedField(
        queryset=Schedule.objects.all(), 
        source='schedule', 
        write_only=True, 
        required=False, 
        allow_null=True
    )
    class Meta:
        model = Doctor
        fields = [
            'id', 'name', 'email', 'phone', 'designation', 'description',
              'image', 'department_id','department', 'department_name', 'department_description',
            'schedule_id', 'schedule', 'schedule_day', 'schedule_time', 'created_by', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        # Extract and remove department_name so it doesn't go to Doctor.objects.create
        department_name = validated_data.pop('department_name', None)
        department_description = validated_data.pop('department_description', None)
        schedule_day = validated_data.pop('schedule_day', None)
        schedule_time = validated_data.pop('schedule_time', None)

        if department_name:
            # Get or create department
            department, created = Department.objects.get_or_create(name=department_name)
            if department_description and department_name:
                department.description = department_description
                department.save()
            validated_data['department'] = department

        if schedule_day:
            schedule, created = Schedule.objects.get_or_create(day=schedule_day)
            if schedule_time and schedule_day:
                schedule.time = schedule_time
                schedule.save()
            validated_data['schedule'] = schedule

        # Now safe to create Doctor without extra fields
        doctor = Doctor.objects.create(**validated_data)
        return doctor
    
    def update(self, instance, validated_data):
        # Extract custom fields
        department_name = validated_data.pop('department_name', None)
        department_description = validated_data.pop('department_description', None)
        schedule_day = validated_data.pop('schedule_day', None)
        schedule_time = validated_data.pop('schedule_time', None)

        # Update Department
        if department_name:
            department, created = Department.objects.get_or_create(name=department_name)
            if department_description:
                department.description = department_description
                department.save()
            instance.department = department
        elif 'department_id' in validated_data:
            instance.department = validated_data.pop('department_id')

        # Update Schedule
        if schedule_day:
            schedule, created = Schedule.objects.get_or_create(day=schedule_day)
            if schedule_time:
                schedule.time = schedule_time
                schedule.save()
            instance.schedule = schedule
        elif 'schedule_id' in validated_data:
            instance.schedule = validated_data.pop('schedule_id')

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
    

class ServiceSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Service
        fields = ['id', 'service_title', 'service_category', 'service_description', 'is_active']


class DepartmentGroupSerializer(serializers.ModelSerializer):

    departments = DepartmentSerializer(many=True, read_only=True)

    department_ids = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Department.objects.all(),
        write_only = True,
        required = False,
    )

    class Meta: 
        model = DepartmentGroup
        fields = ['id', 'group_name', 'departments', 'department_ids']

    def create(self, validated_data):
        department_ids = validated_data.pop('department_ids', [])
        group = DepartmentGroup.objects.create(**validated_data)
        group.departments.set(department_ids)
        return group
    


    def update(self, instance, validated_data):
        department_ids = validated_data.pop('department_ids', None)
        if department_ids is not None:
            instance.departments.set(department_ids)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
