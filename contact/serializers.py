from rest_framework import serializers
from .models import ContactPage, ContactUs


class ContactPageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    total_doctor = serializers.IntegerField(read_only=True)
    doctor_images = serializers.ListField(
        child=serializers.CharField(),
        read_only=True
    )

    class Meta:
        model = ContactPage
        fields = [
            'id',
            'title',
            'sub_title',
            'banner_image_pc',
            'banner_image_tab',
            'banner_image_mob',
            'total_doctor',
            'doctor_images',
            'is_active',
            'created_by',
            'created_at',
            'updated_at',
        ]



class ContactUsSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ContactUs
        fields = '__all__'
