from rest_framework import serializers
from .models import Health_package


class Health_packageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_package
        fields = '__all__'

        