from requests import Response
from rest_framework import serializers
from .models import Appointment, AppointmentBanner, Report
from doctors.models import Doctor, ChamberTime
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

    # schedule = serializers.PrimaryKeyRelatedField(
    #     queryset=ChamberTime.objects.none(),  # 🔥 initially empty
    #     required=False,
    #     allow_null=True
    # )

    class Meta:
        model = Appointment
        fields = [
            "id", "VisitDate",
            "doctor_id",   # write only
            "DrCode",      # read only
            "DrName",      # read only
            "schedule",      

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
        schedule = data.get("schedule")
        visit_date = data.get("VisitDate")
        mobile = data.get("MobileNo")
        dob = data.get("Dob")

        today = date.today()
        max_date = today + timedelta(days=30)   # today + 30 days

        # --- Check 1: Future DOB ---
        if dob and dob > today:
            raise serializers.ValidationError({
                "Dob": "Date of Birth cannot be in the future."
            })

        # --- Check 2: VisitDate range ---
        # if visit_date < today or visit_date > max_date:
        #     raise serializers.ValidationError({
        #         "VisitDate": "You can only book an appointment within the next 30 days."
        #     })

        # --- Check 3: Max 100 appointments per doctor per day ---
        doctor_count = Appointment.objects.filter(
            DrCode=doctor, VisitDate=visit_date
        ).count()
        if doctor_count >= 100:
            raise serializers.ValidationError({
                "msg": "This Doctor's Serial Quota Already Completed. Please Try Another Day."
            })

        # --- Check 4: Same patient can't book same doctor twice same day ---
        existing = Appointment.objects.filter(
            MobileNo=mobile,
            DrCode=doctor,
            VisitDate=visit_date
        ).first()
        if existing:
            # serial_no = str(existing.id).zfill(3)
            raise serializers.ValidationError({
                "msg": f"This number already booked an appointment with this Doctor on same date."
                #  Serial No: {serial_no}
            })

        return data      


    # -------------------------
    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = '__all__'