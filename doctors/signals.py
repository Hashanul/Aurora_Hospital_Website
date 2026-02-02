# doctors/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Department, DoctorImage, Doctor
from home.models import MenuItem, MenuContent


# ===============================
# Department → Menu sync
# ===============================
@receiver(post_save, sender=MenuItem)
def sync_departments_when_menuitem_saved(sender, instance, **kwargs):
    """
    If MenuItem.is_department=True,
    auto attach all Departments as MenuContent
    """

    if not instance.is_department:
        return

    departments = Department.objects.all()

    for dept in departments:
        MenuContent.objects.get_or_create(
            menu=instance,
            department=dept
        )

@receiver(post_save, sender=Department)
def sync_department_to_all_menus(sender, instance, **kwargs):
    """
    When Department is created or updated,
    sync it to all MenuItem where is_department=True
    """

    menus = MenuItem.objects.filter(is_department=True)

    for menu in menus:
        MenuContent.objects.update_or_create(
            menu=menu,
            department=instance
        )


@receiver(post_save, sender=MenuItem)
def cleanup_menucontent_if_menuitem_not_department(sender, instance, **kwargs):
    """
    If a MenuItem is switched from is_department=True to False,
    remove auto-created department MenuContents
    """

    if instance.is_department:
        return

    MenuContent.objects.filter(
        menu=instance,
        department__isnull=False
    ).delete()



@receiver(post_delete, sender=Department)
def delete_department_from_menus(sender, instance, **kwargs):
    """
    When Department is deleted,
    related MenuContent will be deleted automatically
    (CASCADE), but kept here for clarity/safety
    """

    MenuContent.objects.filter(
        department=instance,
        menu__is_department=True
    ).delete()




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