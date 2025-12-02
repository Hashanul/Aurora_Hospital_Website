from rest_framework import serializers
from .models import BOD, ChairmanMessage, MDMessage, AboutBanner


class AboutBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = AboutBanner
        fields = "__all__"

class BODSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = BOD
        fields = "__all__"


class ChairmanMessageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ChairmanMessage
        fields = "__all__"


class MDMessageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = MDMessage
        fields = "__all__"

