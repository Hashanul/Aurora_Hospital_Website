# doctors/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Department, DoctorImage, Doctor
from home.models import MenuItem, MenuContent

# ===============================
# Department → Menu sync
# ===============================
@receiver(post_save, sender=Department)
def sync_menu_content_with_department(sender, instance, created, **kwargs):
    # 🔹 Parent menu
    menu, _ = MenuItem.objects.get_or_create(
        title="Departments",
        defaults={"order": None}
    )

    if created:
        # 🟢 Create MenuContent
        MenuContent.objects.create(
            menu=menu,
            title=instance.name,
            order=instance.order
        )
    else:
        # 🔵 Update MenuContent
        MenuContent.objects.filter(
            menu=menu,
            title=instance.name
        ).update(
            order=instance.order
        )



# ===============================
# DoctorImage delete → Doctor.image NULL
# ===============================
@receiver(post_delete, sender=DoctorImage)
def clear_doctor_image(sender, instance, **kwargs):
    if not instance.drCode:
        return

    try:
        doctor = Doctor.objects.get(drCode=instance.drCode)
        doctor.image = None
        doctor.save(update_fields=['image'])
    except Doctor.DoesNotExist:
        pass