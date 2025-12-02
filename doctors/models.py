from django.db import models
from PIL import Image
from accounts.models import User
from home.models import validate_image_file
from django.utils.text import slugify
from PIL import Image
from django_ckeditor_5.fields import CKEditor5Field
 


class DepartmentBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='department_banner/', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Department Banner : {self.title}"
    
    
class DoctorBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='doctor_banner/', blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Doctor Banner : {self.title}"
    

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(
        upload_to='department/', blank=True, null=True, validators=[validate_image_file])
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        """Generate a unique slug from the department name before saving."""
        if self.name:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            # Ensure unique slug (exclude self when updating)
            while Department.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def total_doctors(self):
        return self.doctors.count()   # related_name='doctors'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    drName = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    richtext = CKEditor5Field(blank=True, null=True)
    image = models.FileField(upload_to='doctor/', blank=True, null=True)
    drCode = models.CharField(max_length=20, null=True, blank=True)

    # Foreign keys
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')

    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15)

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.drName} - ({self.department if self.department else self.id})"


class ChamberTime(models.Model):
    drCode = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    dayName = models.CharField(max_length=100)
    visitType = models.CharField(max_length=100)
    startTime = models.CharField(max_length=100)
    finishTime = models.CharField(max_length=100)

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Doctor: {self.drCode.drName}, Day Name: {self.dayName}"


class BestDoctor(models.Model):
    doctor_name = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, blank=True, null=True, related_name='bestdoctor_name_set')
    best_in_field = models.CharField(max_length=255, null=True, blank=True)
    doctor_image = models.FileField(
        upload_to='best_doctors/', blank=True, null=True)
    doctor_about = models.TextField(blank=True, null=True)
    doctor_skills = models.TextField(
        blank=True, null=True,  help_text="Write skills separated by comma")
    doctor_experiance = models.PositiveIntegerField(blank=True, null=True)

    award_title = models.CharField(max_length=255, blank=True, null=True)
    award_description = models.TextField(null=True, blank=True)
    award_image = models.FileField(
        upload_to='best_doctors_award/', blank=True, null=True)

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_doctor_skills_list(self):
        """Return list of doctor skills (split by comma)."""
        if self.doctor_skills:
            return [h.strip() for h in self.doctor_skills.split(',')]
        return []

    def __str__(self):
        return f"Best Doctor :{self.doctor_name if self.doctor_name else self.id}"


class HomeService(models.Model):
    service_title = models.CharField(max_length=255)
    service_category = models.ForeignKey(
        Department, on_delete=models.SET_NULL, blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)
    service_image = models.FileField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service Title: {self.service_title}"


class DepartmentGroup(models.Model):
    group_name = models.CharField(max_length=250, null=True, blank=True)
    departments = models.ManyToManyField(
        Department, blank=True, related_name='groups')

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group_name if self.group_name else self.id} - {self.departments if self.departments else self.id}"
 