from django.db.models.signals import post_save
from django.dispatch import receiver
from appointment.models import Appointment, Doctor
from award.models import Award
from patients.models import Patient
from .models import Badge

# Helper: get or create badge
def get_badge():
    badge, created = Badge.objects.get_or_create(id=1)
    return badge


# When a new Appointment is created → total_appointment++
@receiver(post_save, sender=Appointment)
def update_appointment_badge(sender, instance, created, **kwargs):
    if created:
        badge = get_badge()
        badge.total_appointment += 1
        badge.save()


# When a new Doctor is created → specialists++
@receiver(post_save, sender=Doctor)
def update_specialists_badge(sender, instance, created, **kwargs):
    if created:
        badge = get_badge()
        badge.specialists += 1
        badge.save()


# When a new Award is created → winning_awards++
@receiver(post_save, sender=Award)
def update_awards_badge(sender, instance, created, **kwargs):
    if created:
        badge = get_badge()
        badge.winning_awards += 1
        badge.save()


# When a new Patient is created → happy_patients++
@receiver(post_save, sender=Patient)
def update_patients_badge(sender, instance, created, **kwargs):
    if created:
        badge = get_badge()
        badge.happy_patients += 1
        badge.save()
