
from django.core.management.base import BaseCommand
from django.db import transaction

from home.models import MenuItem, MenuContent


NAV_DATA = [
    {
        "title": "Home",
        "classChange": "",
        "order": 1,
        "contents": [],
    },
    {
        "title": "About Us",
        "classChange": "sub-menu-down",
        "order": 2,
        "contents": [
            {"title": "About ASHL"},
            {"title": "Message of Chairman"},
            {"title": "Message of Managing Director"},
        ],
    },
    {
        "title": "Our Services",
        "order": 3,
        "to": "/services",
    },
    {
        "title": "Find Doctors",
        "order": 4,
        "to": "/find-doctors",
    },
    {
        "title": "Visitors & Patient",
        "order": 6,
        "classChange": "sub-menu-down",
        "contents": [
            {"title": "Services", "to": "/services"},
            {"title": "Health Check Up"},
            {"title": "Packages"},
            {"title": "Room rent"},
            {"title": "Feedback"},
        ],
    },
    {
        "title": "News",
        "order": 7,
    },
    {
        "title": "Contact",
        "order": 8,
        "to": "/contact-us",
    },
]


class Command(BaseCommand):
    help = "Seed MenuItem and MenuContent navigation data. Idempotent."

    def handle(self, *args, **options):
        created_menus = 0
        created_contents = 0

        with transaction.atomic():
            for item in NAV_DATA:
                # Build defaults only for fields that actually exist on the model
                # and have non-empty values in the NAV_DATA. The NAV_DATA includes
                # an `order` key for ordering purposes, but `MenuItem` does not
                # have an `order` field so we ignore it here.
                defaults = {}
                if "classChange" in item and item.get("classChange"):
                    defaults["classChange"] = item.get("classChange")
                if "to" in item and item.get("to"):
                    defaults["to"] = item.get("to")

                # Create or get by title. Do not pass unknown fields (like order).
                menu, menu_created = MenuItem.objects.get_or_create(
                    title=item["title"], defaults=defaults
                )

                if not menu_created:
                    changed = False
                    # Only update when a non-empty value is provided in NAV_DATA
                    if "classChange" in item and item.get("classChange") and menu.classChange != item.get("classChange"):
                        menu.classChange = item.get("classChange")
                        changed = True
                    if "to" in item and item.get("to") and menu.to != item.get("to"):
                        menu.to = item.get("to")
                        changed = True
                    if changed:
                        menu.save()

                if menu_created:
                    created_menus += 1

                self.stdout.write(self.style.SUCCESS(
                    f"MenuItem: {menu.title} ({'created' if menu_created else 'exists/updated'})"))

                for content in item.get("contents", []):
                    c_defaults = {}
                    if "to" in content:
                        c_defaults["to"] = content.get("to")

                    content_obj, content_created = MenuContent.objects.get_or_create(
                        menu=menu, title=content["title"], defaults=c_defaults
                    )

                    if not content_created:
                        if "to" in content and content_obj.to != content.get("to"):
                            content_obj.to = content.get("to")
                            content_obj.save()

                    if content_created:
                        created_contents += 1

                    self.stdout.write(self.style.SUCCESS(
                        f"  MenuContent: {content_obj.title} ({'created' if content_created else 'exists/updated'})"))

        self.stdout.write(self.style.SUCCESS(
            f"Seeding complete. Menus created: {created_menus}, contents created: {created_contents}"))
