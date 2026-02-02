from rest_framework import serializers
from .models import ContactPage, ContactUs, Contact_data, ContactBanner
from doctors.models import Doctor


class ContactBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model =ContactBanner
        fields = "__all__"


class ContactPageSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    total_doctor = serializers.SerializerMethodField()
    doctor_images = serializers.SerializerMethodField()

    class Meta:
        model = ContactPage
        fields = [
            'id',
            'title',
            'sub_title',
            'total_doctor',
            'doctor_images',
            'is_active',
            'created_by',
            'created_at',
            'updated_at',
        ]

    def get_total_doctor(self, obj):
        return Doctor.objects.count()

    def get_doctor_images(self, obj):
        # Only return the image URL string, no .url needed
        doctors = Doctor.objects.exclude(image='').exclude(image__isnull=True)
        return [doctor.image for doctor in doctors]




class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = '__all__'


class Contact_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_data
        fields = '__all__'