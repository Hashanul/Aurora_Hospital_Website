from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import requests
from .models import Appointment


@receiver(pre_save, sender=Appointment)
def send_appointment_to_external_api(sender, instance, **kwargs):
    # Only for new appointments (creation), not updates
    if instance.pk:
        return

    # Calculate age if not set
    if not instance.AgeYear or not instance.AgeMonth or not instance.AgeDay:
        age_year, age_month, age_day = instance.calculate_age()
        instance.AgeYear = age_year
        instance.AgeMonth = age_month
        instance.AgeDay = age_day

    # Prepare payload for external API
    payload = {
        "VisitDate": str(instance.VisitDate),
        "DrCode": instance.DrCode.drCode if instance.DrCode else "",
        "DrName": instance.DrCode.drName if instance.DrCode else "",
        "PatientName": instance.PatientName,
        "MobileNo": instance.MobileNo,
        "Dob": str(instance.Dob) if instance.Dob else "",
        "AgeDay": instance.AgeDay or "",
        "AgeMonth": instance.AgeMonth or "",
        "AgeYear": instance.AgeYear or "",
        "Sex": instance.Sex,
        "VisitAmount": instance.VisitAmount or "",
        "VisitType": instance.VisitType or "",
    }
    # print(payload)
    try:
        response = requests.post(
            "http://123.253.36.113:9020/API/AppointmentApi/Save", json=payload, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the JSON response
        response_data = response.json()
        # print(response_data)  # For debugging purposes
        # Check the Output field
        if response_data.get("Output") != "success":
            msg = response_data.get("Msg", "Unknown error from external API")
            raise ValidationError(f"External API error: {msg}")

        returnvalue = response_data.get("Returnvalue", {})
        if returnvalue:
            if returnvalue.get("SlNo"):
                instance.SlNo = returnvalue["SlNo"]

    except requests.RequestException as e:
        raise ValidationError(f"Error connecting to external API: {str(e)}")
    except ValueError as e:
        raise ValidationError(
            f"Invalid JSON response from external API: {str(e)}")
