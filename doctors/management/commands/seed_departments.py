from django.core.management.base import BaseCommand
from doctors.models import Department
from home.models import MenuItem

class Command(BaseCommand):
    help = 'Seed the database with initial departments'

    def handle(self, *args, **options):
        # Ensure the MenuItem for 'Our Departments' exists
        menu_item, created = MenuItem.objects.get_or_create(
            title='Our Departments',
            defaults={'to': '/our-departments'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created MenuItem: Our Departments'))
        else:
            self.stdout.write('MenuItem already exists: Our Departments')

        departments_data = [
            {
                'name': 'Cardiology',
                'description': 'Department specializing in heart and cardiovascular diseases.'
            },
            {
                'name': 'Urology',
                'description': 'Department dealing with urinary tract and male reproductive system.'
            },
            {
                'name': 'Neurology',
                'description': 'Department focused on disorders of the nervous system.'
            },
            {
                'name': 'Pediatrics',
                'description': 'Department providing medical care for infants, children, and adolescents.'
            },
            {
                'name': 'Orthopedics',
                'description': 'Department specializing in musculoskeletal system disorders.'
            },
            {
                'name': 'Gynecology',
                'description': 'Department dealing with women\'s reproductive health.'
            },
            {
                'name': 'Dermatology',
                'description': 'Department focused on skin, hair, and nail disorders.'
            },
            {
                'name': 'Radiology',
                'description': 'Department using medical imaging techniques for diagnosis.'
            },
            {
                'name': 'Emergency Medicine',
                'description': 'Department handling urgent medical conditions.'
            },
            {
                'name': 'Oncology',
                'description': 'Department specializing in cancer treatment.'
            },
            {
                'name': 'NICU',
                'description': 'Department specializing in neonatal intensive care.'
            },
            {
                'name': 'ICU',
                'description': 'Department specializing in intensive care.'
            },
            {
                'name': 'Laboratory Medicine',
                'description': 'Department specializing in laboratory tests and diagnostics.'
            },
            {
                'name': 'Vaccination Center',
                'description': 'Department specializing in vaccinations and immunizations.'
            },
            {
                'name': 'Cycatry',
                'description': 'Department specializing in vaccinations and immunizations.'
            },
            {
                'name': 'Emergency',
                'description': 'Department specializing in urgent medical conditions.'
            },
            {
                'name': 'General Surgery',
                'description': 'Department specializing in surgical procedures.'
            },
            {
                'name': 'ENT',
                'description': 'Department specializing in ear, nose, and throat disorders.'
            },
            {
                'name': 'Physiotherapy',
                'description': 'Department specializing in physical therapy and rehabilitation.'
            },
            {
                'name': 'Surgical Oncology',
                'description': 'Department specializing in surgical treatment of cancer.'
            },
        ]

        for dept_data in departments_data:
            department, created = Department.objects.get_or_create(
                name=dept_data['name'],
                defaults={
                    'description': dept_data['description'],
                    'created_by': None  # Assuming no default user for seeding
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created department: {department.name}'))
            else:
                self.stdout.write(f'Department already exists: {department.name}')