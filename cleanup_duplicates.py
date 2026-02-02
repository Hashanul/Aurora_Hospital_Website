# save this as cleanup_duplicates.py or run in shell

from nav.models import MenuContent
from django.db.models import Count

# 1️⃣ Find duplicate (menu, department) pairs
duplicates = (
    MenuContent.objects
    .values('menu', 'department')
    .annotate(c=Count('id'))
    .filter(c__gt=1)
)

print(f"Found {duplicates.count()} duplicate pairs.")

# 2️⃣ Delete duplicates (keep the first one)
for dup in duplicates:
    menu_id = dup['menu']
    dept_id = dup['department']

    contents = MenuContent.objects.filter(menu_id=menu_id, department_id=dept_id).order_by('id')

    # keep the first, delete rest
    to_delete = contents[1:]
    count = to_delete.count()
    to_delete.delete()
    print(f"Deleted {count} duplicates for menu={menu_id}, department={dept_id}")

print("✅ Duplicate cleanup completed.")
