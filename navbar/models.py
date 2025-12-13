# from django.db import models
# from accounts.models import User
# from django.utils.text import slugify





# class PopUp(models.Model):
#     title = models.CharField(max_length=255)
#     image = models.FileField(upload_to='popup_image/', blank=True, null=True)

#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True) 


#     def __str__(self):
#         return self.title


# class MenuItem(models.Model):
#     title = models.CharField(max_length=255)
#     to = models.CharField(max_length=255, blank=True, null=True)
#     classChange = models.CharField(max_length=100, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.to:
#             self.to = "/" + slugify(self.title)
#         super().save(*args, **kwargs)

 
#     def __str__(self):
#         return self.title


# class MenuContent(models.Model):
#     menu = models.ForeignKey(
#         MenuItem,
#         related_name="content",
#         on_delete=models.CASCADE
#     ) 

#     # these appear INSIDE content[] array
#     title = models.CharField(max_length=255)
#     to = models.CharField(max_length=255, blank=True, null=True)
#     # type = models.CharField(max_length=255, choices=TYPE_CHOICE, null=True, blank=True)


#     def save(self, *args, **kwargs):
#         if not self.to:
#             # Example output: "Main-Menu/about-us"
#             self.to = f"/{slugify(self.menu.title)}/{slugify(self.title)}"
#         super().save(*args, **kwargs)


#     def __str__(self):
#         return f"Content: {self.title} → Menu:{self.menu.title}"