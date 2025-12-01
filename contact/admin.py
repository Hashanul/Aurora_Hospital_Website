from django.contrib import admin
from .models import ContactBanner, ContactPage, ContactUs, Contact_data


@admin.register(ContactBanner)
class ContactBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'sub_title']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'message']
    list_filter = ['email', 'phone', 'subject', 'message']
    search_fields = ['email', 'phone', 'subject', 'message']


@admin.register(Contact_data)
class Contact_dataAdmin(admin.ModelAdmin):
    list_display = ['hotline', 'address', 'email', 'fb_link', 'linkedin', 'youtub', 'x_link', 'instra_link']
    search_fields = ['hotline', 'address', 'email', 'fb_link', 'linkedin', 'youtub', 'x_link', 'instra_link']
