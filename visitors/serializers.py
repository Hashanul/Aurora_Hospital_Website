from rest_framework import serializers
from .models import RoomRent, Equipment, FeedbackBanner, Feedback



class RoomRentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = RoomRent
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Equipment
        fields = '__all__'

class FeedbackBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = FeedbackBanner
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Feedback
        fields = '__all__'

