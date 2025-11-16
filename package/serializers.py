from rest_framework import serializers
from .models import Health_package


class Health_packageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Health_package
        fields = '__all__'

        