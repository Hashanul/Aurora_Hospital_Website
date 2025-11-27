from django.db import models
from doctors.models import Department, Doctor



class Appointment(models.Model):

    GENDER_CHOICES=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    VisitDate = models.DateField()
    DrCode = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True, related_name='appointments_by_code')
    DrName = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments_by_name')

    PatientName = models.CharField(max_length=255, )
    MobileNo = models.CharField(max_length=15)
    PatientEmail = models.EmailField(null=True, blank=True)

    Dob = models.DateField(blank=True, null=True)
    AgeDay = models.PositiveIntegerField(blank=True, null=True)
    AgeMonth = models.PositiveIntegerField(blank=True, null=True)
    AgeYear = models.PositiveIntegerField(blank=True, null=True)

    Sex = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    VisitAmount = models.IntegerField(blank=True, null=True)

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

        # year
        age_year = visit.year - dob.year

        # adjust if birthday not passed
        if (visit.month, visit.day) < (dob.month, dob.day):
            age_year -= 1

        # month
        age_month = visit.month - dob.month
        if age_month < 0:
            age_month += 12
        if visit.day < dob.day:
            age_month -= 1

        # days
        if visit.day >= dob.day:
            age_day = visit.day - dob.day
        else:
            # previous month days
            from calendar import monthrange
            prev_month_days = monthrange(visit.year, visit.month - 1)[1]
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