# departments/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Department
from home.models import MenuItem, MenuContent   # adjust import path

@receiver(post_save, sender=Department)
def create_menu_content_for_department(sender, instance, created, **kwargs):
    if created:
        print(instance)
        department_name = instance.name
        menu = MenuItem.objects.get(title='Our Departments')
        MenuContent.objects.create(
            menu=menu,
            title=department_name,
        )
 
