from django.core.management.base import BaseCommand
from doctors.models import Department, DepartmentGroup
from home.models import MenuItem


class Command(BaseCommand):
    help = "Seed the database with initial departments"

    def handle(self, *args, **options):
        # Ensure the MenuItem for 'Our Departments' exists
        menu_item, created = MenuItem.objects.get_or_create(
            title="Our Departments", defaults={"to": "/our-departments"}
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Created MenuItem: Our Departments"))
        else:
            self.stdout.write("MenuItem already exists: Our Departments")

        departments_data = [
            {
                "name": "Medicine & Rheumatology",
                "description": "Providing services for Medicine & Rheumatology.",
            },
            {
                "name": "Medicine",
                "description": "Providing services for Medicine.",
            },
            {
                "name": "Neuro-Medicine",
                "description": "Providing services for Neuro-Medicine.",
            },
            {
                "name": "Gastroenterology",
                "description": "Providing services for Gastroenterology.",
            },
            {
                "name": "General Surgery",
                "description": "Providing services for General Surgery.",
            },
            {
                "name": "Neuro-Surgery",
                "description": "Providing services for Neuro-Surgery.",
            },
            {
                "name": "Orthopedic",
                "description": "Providing services for Orthopedic.",
            },
            {
                "name": "ENT & Head-Neck Surgery",
                "description": "Providing services for ENT & Head-Neck Surgery.",
            },
            {
                "name": "Hepatobiliary Surgery",
                "description": "Providing services for Hepatobiliary Surgery.",
            },
            {
                "name": "Hepatology",
                "description": "Providing services for Hepatology.",
            },
            {
                "name": "Urology",
                "description": "Providing services for Urology.",
            },
            {
                "name": "Gynecology & Obstetrics",
                "description": "Providing services for Gynecology & Obstetrics.",
            },
            {
                "name": "Gynecology, Obstetrics & Infertility",
                "description": "Providing services for Gynecology, Obstetrics & Infertility.",
            },
            {
                "name": "Neonatal & Pediatric",
                "description": "Providing services for Neonatal & Pediatric.",
            },
            {
                "name": "Pediatric Neurology",
                "description": "Providing services for Pediatric Neurology.",
            },
            {
                "name": "Pediatric Gastro, Liver & Nutrition",
                "description": "Providing services for Pediatric Gastro, Liver & Nutrition.",
            },
            {
                "name": "Pediatric Nephrology",
                "description": "Providing services for Pediatric Nephrology.",
            },
            {
                "name": "Pediatric Surgery",
                "description": "Providing services for Pediatric Surgery.",
            },
            {
                "name": "Cardiology",
                "description": "Providing services for Cardiology.",
            },
            {
                "name": "Diabetes & Endocrinology",
                "description": "Providing services for Diabetes & Endocrinology.",
            },
            {
                "name": "Nephrology",
                "description": "Providing services for Nephrology.",
            },
            {
                "name": "Hematology",
                "description": "Providing services for Hematology.",
            },
            {
                "name": "Infectious Disease",
                "description": "Providing services for Infectious Disease.",
            },
            {
                "name": "Thoracic Surgery",
                "description": "Providing services for Thoracic Surgery.",
            },
            {
                "name": "Burn & Plastic Surgery",
                "description": "Providing services for Burn & Plastic Surgery.",
            },
            {
                "name": "Ophthalmology",
                "description": "Providing services for Ophthalmology.",
            },
            {
                "name": "Oncology (Cancer)",
                "description": "Providing services for Oncology (Cancer).",
            },
            {
                "name": "Cancer Surgery",
                "description": "Providing services for Cancer Surgery.",
            },
            {
                "name": "Dental",
                "description": "Providing services for Dental.",
            },
            {
                "name": "Food & Nutrition",
                "description": "Providing services for Food & Nutrition.",
            },
            {
                "name": "Psychiatry",
                "description": "Providing services for Psychiatry.",
            },
            {
                "name": "Dermatology & Venereology",
                "description": "Providing services for Dermatology & Venereology.",
            },
            {
                "name": "Physical Medicine & Rehabilitation",
                "description": "Providing services for Physical Medicine & Rehabilitation.",
            },
            {
                "name": "Laboratory",
                "description": "Providing services for Laboratory.",
            },
            {
                "name": "Interventional Radiology",
                "description": "Providing services for Interventional Radiology.",
            },
            {
                "name": "Anesthesia & Pain Medicine",
                "description": "Providing services for Anesthesia & Pain Medicine.",
            },
            {
                "name": "Psychotherapy",
                "description": "Providing services for Psychotherapy.",
            },
        ]

        for dept_data in departments_data:
            department, created = Department.objects.get_or_create(
                name=dept_data["name"],
                defaults={
                    "description": dept_data["description"],
                    "created_by": None,  # Assuming no default user for seeding
                },
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully created department: {department.name}"
                    )
                )
            else:
                self.stdout.write(f"Department already exists: {department.name}")

        # Create DepartmentGroup with all departments
        group, created = DepartmentGroup.objects.get_or_create(
            group_name="Hospital Departments", defaults={"created_by": None}
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS("Created DepartmentGroup: Hospital Departments")
            )
        else:
            self.stdout.write("DepartmentGroup already exists: Hospital Departments")

        # Get all departments and add to the group
        departments = Department.objects.all()
        group.departments.set(departments)
        self.stdout.write(self.style.SUCCESS("Added all departments to the group"))

        # Create specific DepartmentGroups and assign relevant departments
        groups_mapping = {
            "Head": [
                "Ophthalmology",
                "Neuro-Medicine",
                "Neuro-Surgery",
                "ENT & Head-Neck Surgery",
                "Pediatric Neurology",
            ],
            "Throat": [
                "ENT & Head-Neck Surgery",
                "Dental",
            ],
            "Chest": [
                "Thoracic Surgery",
                "Cardiology",
            ],
            "Upper_GI": [
                "Gastroenterology",
                "Hepatobiliary Surgery",
                "Hepatology",
                "Interventional Radiology",
            ],
            "Lower_Abdomen": [
                "General Surgery",
                "Urology",
                "Nephrology",
                "Cancer Surgery",
            ],
            "Female_Lower_Abdomen": [
                "General Surgery",
                "Urology",
                "Nephrology",
                "Cancer Surgery",
                "Gynecology & Obstetrics",
                "Gynecology, Obstetrics & Infertility",
            ],
            "Orthopaedics": [
                "Orthopedic",
                "Dermatology & Venereology",
                "Physical Medicine & Rehabilitation",
            ],
        }

        for grp_name, dept_names in groups_mapping.items():
            grp, created = DepartmentGroup.objects.get_or_create(
                group_name=grp_name, defaults={"created_by": None}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created DepartmentGroup: {grp_name}")
                )
            else:
                self.stdout.write(f"DepartmentGroup already exists: {grp_name}")

            # Find departments by name and set the group's departments
            matched = Department.objects.filter(name__in=dept_names)
            grp.departments.set(matched)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Assigned {matched.count()} departments to group: {grp_name}"
                )
            )
