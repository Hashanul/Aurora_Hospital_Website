from rest_framework import serializers
from .models import Health_package, Health_Service


class Health_packageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Health_package
        fields = '__all__'

class Health_ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Service
        fields = '__all__'

