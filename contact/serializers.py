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

    # Return total number of doctors
    def get_total_doctor(self, obj):
        return Doctor.objects.count()

    # Return list of doctor image URLs
    def get_doctor_images(self, obj):
        doctors = Doctor.objects.exclude(image='')
        return [doctor.image.url for doctor in doctors if doctor.image]





class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = '__all__'


class Contact_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_data
        fields = '__all__'