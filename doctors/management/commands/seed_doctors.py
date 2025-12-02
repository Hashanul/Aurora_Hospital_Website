from django.core.management.base import BaseCommand
from doctors.models import Doctor, Department


class Command(BaseCommand):
    help = "Seed the database with initial doctors"

    def handle(self, *args, **options):
        # Doctors data grouped by department
        doctors_data = [
            # Medicine & Rheumatology Department
            {
                "drName": "Dr. Md. Nahiduzzaman Sajjad",
                "designation": "MBBS, FCPS (Medicine), MD (Rheumatology); EULAR Certified",
                "description": (
                    "Member, American College of Physicians. Medicine and Rheumatology Specialist. "
                    "Advanced training in gout, back, shoulder, neck and muscle pain diseases. "
                    "Associate Professor, Bangladesh Medical University (Former PG Hospital)."
                ),
                "department_name": "Medicine & Rheumatology",
            },
            {
                "drName": "Dr. Md. Main Uddin Sohel",
                "designation": "MBBS, BCS (Health), FCPS (Medicine), MCPS (Medicine), MRCP (UK), MD Rheumatology (BMU)",
                "description": "Consultant, Medicine and Rheumatology.",
                "department_name": "Medicine & Rheumatology",
            },
            {
                "drName": "Dr. Md. Atikur Rahman",
                "designation": "MBBS, BCS (Health), MD (Rheumatology) BM&U, FACR (USA)",
                "description": "EULAR Certified Rheumatologist. Consultant Rheumatologist, Central Police Hospital, Rajarbag, Dhaka. BMDC Reg. No. A-67816",
                "department_name": "Medicine & Rheumatology",
            },
            # Medicine Department
            {
                "drName": "Professor Dr. Richmond Ronald Gomez",
                "designation": "MBBS (DMC), FACP (USA), FCPS (Medicine)",
                "description": "Professor and Head of Department, Internal Medicine Department, Ad-din Medical College Hospital.",
                "department_name": "Medicine",
            },
            {
                "drName": "Dr. Kazi Ismail Hosen",
                "designation": "MBBS, BCS (Health), FCPS (Medicine), MACP (America), MD (Critical Care Medicine)",
                "description": "Internist and Intensivist. Medicine and ICU Specialist at National Institute of Neurosciences and Hospital.",
                "department_name": "Medicine",
            },
            {
                "drName": "Dr. Md. Abul Kashem Azad",
                "designation": "MBBS (Dhaka), CCD (BIRDEM)",
                "description": "Senior Family Medicine Physician. Former Registrar Medicine Unit, Dhaka Medical College Hospital.",
                "department_name": "Medicine",
            },
            # Neuro-Medicine Department
            {
                "drName": "Dr. Md. Ziaul Haque (Bablu)",
                "designation": "MBBS (CMC), BCS (Health), MCPS (Medicine), MRCP (UK), MD (Neurology)",
                "description": "Medicine, Neuro-Medicine, Neurology, Stroke, Rheumatology and Diabetes Specialist. Registrar Neurology, Shaheed Suhrawardy Medical College Hospital, Dhaka. BMDC Reg. No: A-66479",
                "department_name": "Neuro-Medicine",
            },
            {
                "drName": "Dr. Md. Abdul Bari",
                "designation": "MBBS (SSMC), CCD (BIRDEM), MD (Neurology)",
                "description": "Neuromedicine Specialist. Specialist in headache, dizziness, stroke, paralysis, dementia, epilepsy and spinal pain. BMDC Reg. No: A-43740",
                "department_name": "Neuro-Medicine",
            },
            {
                "drName": "Dr. Md. Samsuzzaman",
                "designation": "MBBS, BCS (Health), MD (Neurology)",
                "description": "Neurologist, Interventional Neurology Department, National Institute of Neurosciences and Hospital. Specialist in headache, seizure, paralysis and stroke.",
                "department_name": "Neuro-Medicine",
            },
            # Gastroenterology Department
            {
                "drName": "Professor Dr. Md. Habibur Rahman",
                "designation": "MBBS, FCPS (Medicine), MD (Gastroenterology)",
                "description": "Former Professor and Head of Department, Gastroenterology Department, Sir Salimullah Medical College and Mitford Hospital.",
                "department_name": "Gastroenterology",
            },
            {
                "drName": "Professor (Dr.) Md. Saif Uddoula",
                "designation": "MBBS (DMC), MCPS (Medicine), MD (Gastroenterology)",
                "description": "Medicine, digestive system and liver disease specialist. Director and Professor, National Gastroliver Institute and Hospital, Dhaka.",
                "department_name": "Gastroenterology",
            },
            {
                "drName": "Professor Dr. Ali Mansur (Sharif)",
                "designation": "MBBS, MD (Gastroenterology)",
                "description": "Professor and Head of Department, Gastroenterology Department, Dhaka Medical College Hospital. BMDC Reg. No: A-25610",
                "department_name": "Gastroenterology",
            },
        ]

        created_count = 0
        for data in doctors_data:
            dept_name = data.pop("department_name", None)
            department = None
            if dept_name:
                department = Department.objects.filter(name__iexact=dept_name).first()

            defaults = {
                "designation": data.get("designation"),
                "description": data.get("description"),
                "department": department,
                "created_by": None,
            }

            doctor, created = Doctor.objects.get_or_create(
                drName=data["drName"], defaults=defaults
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Created doctor: {doctor.drName}")
                )
            else:
                # Update department/designation/description if changed
                updated = False
                if department and doctor.department != department:
                    doctor.department = department
                    updated = True
                if (
                    defaults["designation"]
                    and doctor.designation != defaults["designation"]
                ):
                    doctor.designation = defaults["designation"]
                    updated = True
                if (
                    defaults["description"]
                    and doctor.description != defaults["description"]
                ):
                    doctor.description = defaults["description"]
                    updated = True
                if updated:
                    doctor.save()
                    self.stdout.write(
                        self.style.SUCCESS(f"Updated doctor: {doctor.drName}")
                    )
                else:
                    self.stdout.write(f"Doctor already exists: {doctor.drName}")

        self.stdout.write(
            self.style.SUCCESS(f"Doctors seeding finished. Created: {created_count}")
        )
