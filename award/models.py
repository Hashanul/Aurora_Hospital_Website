from django.db import models
from accounts.models import User




class Award(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    year = models.PositiveIntegerField()

    pc_image = models.ImageField(upload_to='award/', null=True, blank=True)
    tab_image = models.ImageField(upload_to='award/', null=True, blank=True)
    mobile_image = models.ImageField(upload_to='award/', null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Award : {self.title}"
    