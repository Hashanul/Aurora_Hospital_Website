from requests import Response
from rest_framework import serializers
from .models import Appointment, AppointmentBanner
from doctors.models import Doctor
from datetime import date
from datetime import date, timedelta


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

        doctor = data.get("DrCode")
        visit_date = data.get("VisitDate")
        mobile = data.get("MobileNo")

        today = date.today()
        max_date = today + timedelta(days=7)   # today + 7 days

        # Rule 1: Date range validation (Today → Today+7)
        if visit_date < today or visit_date > max_date:
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

        # Rule 3: Same patient can't book same doctor twice on same date
        existing = Appointment.objects.filter(
            MobileNo=mobile,
            DrCode=doctor,
            VisitDate=visit_date
        ).first()

        if existing:
            serial_no = str(existing.id).zfill(3)
            raise serializers.ValidationError({
                "msg": f"This number already booked an appointment with this Doctor on same date. Serial No: {serial_no}"
            })


        return data

    # -------------------------
    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)
