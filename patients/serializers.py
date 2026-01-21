from rest_framework import serializers
from .models import Patient, PatientBanner, PatientStory, PatientStoryBanner
from doctors.models import Doctor, Department



class PatientBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = PatientBanner
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

        
class PatientStoryBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = PatientStoryBanner
        fields = '__all__'


class PatientStorySerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    department = serializers.StringRelatedField(read_only=True)
    doctor = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = PatientStory
        fields = '__all__'

    
        
    def to_representation(self, instance):
        """
        Convert doctor ID → doctor name in response
        """
        data = super().to_representation(instance)

        if instance.doctor:
            data['doctor'] = str(instance.doctor.drName)
        else:
            data['doctor'] = None

        return data

