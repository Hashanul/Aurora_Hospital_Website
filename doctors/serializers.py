from rest_framework import serializers
from .models import Doctor, BestDoctor, Department, ChamberTime, HomeService, DepartmentGroup, DoctorBanner, DepartmentBanner


class DepartmentBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = DepartmentBanner
        fields = '__all__'


class DoctorBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = DoctorBanner
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    total_doctors = serializers.IntegerField(read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Department
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

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
 
    # chamber_time = serializers.StringRelatedField(read_only=True)
    # chamber_time_id = serializers.PrimaryKeyRelatedField(
    #     queryset=ChamberTime.objects.all(), 
    #     source='chamber_time', 
    #     write_only=True, 
    #     required=False, 
    #     allow_null=True
    # )
    class Meta:
        model = Doctor
        fields = [
            'id', 'drName', 'email', 'phone', 'designation', 'description', 'drCode', 'richtext',
              'image', 'department_id','department', 'department_name', 'department_description',
             'created_by', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        # Extract and remove department_name so it doesn't go to Doctor.objects.create
        department_name = validated_data.pop('department_name', None)
        department_description = validated_data.pop('department_description', None)

        if department_name:
            # Get or create department
            department, created = Department.objects.get_or_create(name=department_name)
            if department_description and department_name:
                department.description = department_description
                department.save()
            validated_data['department'] = department

        # Now safe to create Doctor without extra fields
        doctor = Doctor.objects.create(**validated_data)
        return doctor
    
    def update(self, instance, validated_data):
        # Extract custom fields
        department_name = validated_data.pop('department_name', None)
        department_description = validated_data.pop('department_description', None)

        # Update Department
        if department_name:
            department, created = Department.objects.get_or_create(name=department_name)
            if department_description:
                department.description = department_description
                department.save()
            instance.department = department
        elif 'department_id' in validated_data:
            instance.department = validated_data.pop('department_id')
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
    
class ChamberTimeSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    drCode = serializers.CharField(source='drCode.drCode', read_only=True)  
    drName = serializers.CharField(source='drCode.drName', read_only=True)  
    drCode_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(),
        source='drCode',
        write_only=True 
    )

    class Meta:
        model = ChamberTime
        fields = [
            'id','drCode_id','drCode', 'drName','dayName','visitType',
            'startTime','finishTime','created_by','created_at','updated_at'
        ]
    

class BestDoctorSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    doctor_name = serializers.StringRelatedField()

    doctor_skills_list = serializers.SerializerMethodField()

    class Meta:
        model = BestDoctor
        fields = ['id', 'doctor_name', 'best_in_field', 'doctor_image', 'doctor_about', 'doctor_skills', 'doctor_skills_list', 'doctor_experiance', 'award_title', 'award_description', 'award_image', 'created_by']
        extra_kwargs = {
            'doctor_skills': {'write_only': True}
        }

    def get_doctor_skills_list(self, obj):
        return obj.get_doctor_skills_list()


class HomeServiceSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
   
    class Meta:
        model = HomeService
        fields = ['id', 'service_title', 'service_category', 'service_description', 'service_image', 'is_active', 'created_by']


class DepartmentGroupSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    departments = DepartmentSerializer(many=True, read_only=True)

    department_ids = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Department.objects.all(),
        write_only = True,
        required = False,
    )

    class Meta: 
        model = DepartmentGroup
        fields = ['id', 'group_name', 'departments', 'department_ids', 'created_by']

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
 