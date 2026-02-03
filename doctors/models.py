from django.db import models
from PIL import Image
from accounts.models import User
# from home.models import validate_image_file
from django.utils.text import slugify
from PIL import Image
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models import F
from django.conf import settings

 

class DepartmentBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='departments_banner/', blank=True, null=True)

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
    

class HomeDepartmentHeader(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.title if self.title else self.id}"


class HomeDoctorHeader(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.title if self.title else self.id}"


class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    banner = models.FileField(upload_to='department_banner/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    richtext = CKEditor5Field(blank=True, null=True)
    image = models.FileField(
        upload_to='department/', blank=True, null=True )
    order = models.PositiveIntegerField(null=True, blank=True)
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
    
    class Meta:
        ordering = [F('order').asc(nulls_last=True)]

    def __str__(self):
        return self.name if self.name else self.id
 


class DoctorImage(models.Model):
    dr_image = models.FileField(upload_to='doctor/', null=True, blank=True)
    drCode = models.CharField(max_length=20, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.drCode:
            return

        try:
            doctor = Doctor.objects.get(drCode=self.drCode)
        except Doctor.DoesNotExist:
            return

        # 🔹 If image exists → update Doctor.image
        if self.dr_image:
            doctor.image = f"{settings.BASE_URL}{self.dr_image.url}"
        else:
            doctor.image = None

        doctor.save(update_fields=['image'])

    def __str__(self):
        return f"{self.drCode if self.drCode else self.id}"
    


class Doctor(models.Model):
    title = models.CharField(max_length=255)
    drName = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    richtext = CKEditor5Field(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    drCode = models.CharField(max_length=20, null=True, blank=True)

    # Foreign keys
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')

    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_doctor = models.BooleanField(default=True)


    ## additional fields
    drStatus = models.CharField(max_length=100, blank=True, null=True)
    takeCom = models.PositiveIntegerField(blank=True, null=True)
    drType = models.CharField(max_length=100, blank=True, null=True)
    sms = models.PositiveIntegerField(blank=True, null=True)

    order = models.PositiveIntegerField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = [F('order').asc(nulls_last=True), '-created_at']


    def __str__(self):
        return f"{self.drName if self.drName else self.id} - DrCode : {self.drCode} "


class ChamberTime(models.Model):
    drCode = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    dayName = models.CharField(max_length=100)
    visitType = models.CharField(max_length=100, blank=True, null=True)
    startTime = models.CharField(max_length=100, blank=True, null=True)
    finishTime = models.CharField(max_length=100, blank=True, null=True)

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Doctor: {self.drCode if self.drCode else self.id}, Day Name: {self.dayName}"


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





class DepartmentGroup(models.Model):
    group_name = models.CharField(max_length=250, blank=True, null=True)
    departments = models.ManyToManyField(
        Department, blank=True, related_name='groups')

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group_name if self.group_name else self.id}"
 