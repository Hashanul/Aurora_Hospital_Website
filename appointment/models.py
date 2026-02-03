from django.db import models
from home.models import Health_package
from doctors.models import Department, Doctor, ChamberTime
from accounts.models import User
from calendar import monthrange




class AppointmentBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='appointment_banner/', null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment Banner : {self.title}"
 

class Appointment(models.Model):

    GENDER_CHOICES=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    VisitDate = models.DateField()
    DrCode = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True, related_name='appointments_by_code')
    DrName = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments_by_name')
    schedule = models.ForeignKey(ChamberTime, on_delete=models.SET_NULL, blank=True, null=True)
    
    PatientName = models.CharField(max_length=255, )
    MobileNo = models.CharField(max_length=15)
    PatientEmail = models.EmailField(null=True, blank=True)

    Dob = models.DateField(blank=True, null=True)
    AgeDay = models.PositiveIntegerField(blank=True, null=True)
    AgeMonth = models.PositiveIntegerField(blank=True, null=True)
    AgeYear = models.PositiveIntegerField(blank=True, null=True)

    Sex = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    VisitAmount = models.CharField(max_length=20, blank=True, null=True)
    VisitType = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def calculate_age(self):
        """Calculate age on VisitDate."""
        if not self.Dob or not self.VisitDate:
            return None, None, None

        dob = self.Dob
        visit = self.VisitDate

        # -------- YEAR --------
        age_year = visit.year - dob.year
        if (visit.month, visit.day) < (dob.month, dob.day):
            age_year -= 1

        # -------- MONTH --------
        age_month = visit.month - dob.month
        if visit.day < dob.day:
            age_month -= 1
        if age_month < 0:
            age_month += 12

        # -------- DAY --------
        if visit.day >= dob.day:
            age_day = visit.day - dob.day
        else:
            # 🔥 FIX HERE (January safe)
            if visit.month == 1:
                prev_month = 12
                prev_year = visit.year - 1
            else:
                prev_month = visit.month - 1
                prev_year = visit.year

            prev_month_days = monthrange(prev_year, prev_month)[1]
            age_day = prev_month_days - (dob.day - visit.day)

        return age_year, age_month, age_day


    def save(self, *args, **kwargs):
        # Auto-calc age before save
        y, m, d = self.calculate_age()
        self.AgeYear = y
        self.AgeMonth = m
        self.AgeDay = d

        super().save(*args, **kwargs)


    def __str__(self):
        return f"Appointment Information: {self.PatientName} - {self.DrName} ({self.VisitDate})"
    

class Report(models.Model):
    patient_id = models.CharField(max_length=100)
    report_file = models.FileField(upload_to="report", null=True, blank=True)

    def __str__(self):
        return self.patient_id
    


class AppointmentPackageBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='appointmentPackage_banner/', null=True, blank=True)

    def __str__(self):
        return f"Appointment Banner : {self.title if self.title else self.id}"
    

class AppointmentPackage(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    patient_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    request_for = models.TextField(blank=True, null=True)
    health_package = models.ForeignKey(
        Health_package, on_delete=models.CASCADE, related_name="appointments"
    )

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.health_package.title}"
    

class AppointmentPackageHeader(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.title if self.title else self.id}"
