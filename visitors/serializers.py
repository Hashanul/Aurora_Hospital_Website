from rest_framework import serializers
from .models import RoomRent, FeedbackBanner, Feedback



class RoomRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomRent
        fields = '__all__'


class FeedbackBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackBanner
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

