from rest_framework import serializers
from .models import Award


class AwardSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Award
        fields = '__all__'
