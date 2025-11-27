from django.db import models
from accounts.models import User
from PIL import Image
from django_ckeditor_5.fields import CKEditor5Field

class NewsCategories(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='news_title_image/', null=True, blank=True)
    richtext = CKEditor5Field('Content', config_name='default', blank=True, null=True)
    category = models.ForeignKey(NewsCategories, on_delete=models.SET_NULL, null=True, blank=True, related_name='news')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
     
     