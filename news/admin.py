from django.contrib import admin
from .models import NewsBanner, News, NewsCategories



@admin.register(NewsBanner)
class NewsBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_by']
    search_fields = ['title']

@admin.register(NewsCategories)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'richtext', 'category']
    list_filter = ['category']
    search_fields = ['title', 'richtext']
