# doctors/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Department
from home.models import MenuItem, MenuContent


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

