from requests import Response
from rest_framework import serializers
from .models import Appointment, AppointmentBanner
from doctors.models import Doctor
from datetime import date


class AppointmentBannerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = AppointmentBanner
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):

    # Accept doctor by ID (write only)
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.filter(drCode__isnull=False),
        source="DrCode",
        write_only=True,
        allow_null=True,
        required=False
    )

    # Return doctor code (read)
    DrCode = serializers.CharField(source="DrCode.drCode", read_only=True)

    # Return doctor name (read)
    DrName = serializers.CharField(source="DrCode.drName", read_only=True)

    class Meta:
        model = Appointment
        fields = [
            "id", "VisitDate",
            "doctor_id",   # write only
            "DrCode",      # read only
            "DrName",      # read only

            "PatientName", "MobileNo", "PatientEmail",
            "Dob", "AgeDay", "AgeMonth", "AgeYear",
            "Sex", "VisitAmount", "VisitType",
            "created_at", "updated_at",
        ]
        read_only_fields = ["AgeDay", "AgeMonth", "AgeYear"]

    # -------------------------
    # VALIDATION RULES
    # -------------------------
    def validate(self, data):

        doctor = data.get("DrCode")  # doctor instance (from doctor_id)
        visit_date = data.get("VisitDate")
        mobile = data.get("MobileNo")

        # Rule 1: Only today's appointment allowed
        if visit_date != date.today():
            raise serializers.ValidationError({
                "msg": "You wouldn't make Advance appointment of this Doctor."
            })

        # Rule 2: Max 100 appointments per doctor per day
        doctor_count = Appointment.objects.filter(
            DrCode=doctor, VisitDate=visit_date
        ).count()

        if doctor_count >= 100:
            raise serializers.ValidationError({
                "msg": "This Doctor Serial Quota Already Completed. Please Try for Another Day."
            })

        # Rule 3: Same mobile cannot book twice on same date
        existing = Appointment.objects.filter(
            MobileNo=mobile,
            VisitDate=visit_date
        ).first()

        if existing:
            serial_no = str(existing.id).zfill(3)
            raise serializers.ValidationError({
                "msg": f"Already appointed With this Mobile No and serial no is {serial_no}"
            })

        return data

    # -------------------------
    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)
