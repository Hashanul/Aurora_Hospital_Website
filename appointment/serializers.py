
from rest_framework import serializers
from .models import Appointment
from doctors.models import Doctor
from datetime import date


class AppointmentSerializer(serializers.ModelSerializer):

    DrCode_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(),
        source='DrCode',
        write_only=True,
        required=False
    )
    DrName_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(),
        source='DrName',
        write_only=True,
        required=False
    )

    DrCode = serializers.CharField(source="DrCode.drCode", read_only=True)
    DrName = serializers.CharField(source="DrName.drName", read_only=True)

    class Meta:
        model = Appointment
        fields = [
            "id", "VisitDate", 'DrCode_id', "DrName_id", "DrCode", "DrName",
            "PatientName", "MobileNo", "PatientEmail",
            "Dob", "AgeDay", "AgeMonth", "AgeYear",
            "Sex", "VisitAmount", "VisitType",
            "created_at", "updated_at",
        ]
        read_only_fields = ["AgeDay", "AgeMonth", "AgeYear"]

    # -------------------------
    # Doctor linking auto-fix
    # -------------------------
    def _sync_doctors(self, validated_data):
        dr_code = validated_data.get("DrCode")
        dr_name = validated_data.get("DrName")

        if dr_code and not dr_name:
            validated_data["DrName"] = dr_code

        if dr_name and not dr_code:
            validated_data["DrCode"] = dr_name

        return validated_data

    # -------------------------
    # VALIDATION RULES
    # -------------------------
    def validate(self, data):

        data = self._sync_doctors(data)

        doctor = data.get("DrCode") or data.get("DrName")
        visit_date = data.get("VisitDate")
        mobile = data.get("MobileNo")

        # Rule 1: Only today's appointment allowed
        if visit_date != date.today():
            raise serializers.ValidationError({
                "msg": "You wouldn't make Advance appointment of this Doctor."
            })

        # Rule 2: Max 10 appointments per doctor per day
        doctor_count = Appointment.objects.filter(
            DrCode=doctor, VisitDate=visit_date
        ).count()

        if doctor_count >= 5 :
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
        validated_data = self._sync_doctors(validated_data)
        return Appointment.objects.create(**validated_data)
