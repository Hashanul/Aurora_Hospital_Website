from rest_framework import serializers
from .models import ContactPage, ContactUs, Contact_data, ContactBanner


class ContactBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model =ContactBanner
        fields = "__all__"



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


class Contact_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_data
        fields = '__all__'