from django.contrib import admin
from django.http import HttpRequest

from account_module.models import User
from my_method_module.my_slug import get_unique_slug
from . import models
from .models import Blog


# Register your models here.


@admin.register(models.BlogTag)
class AdminBlogTag(admin.ModelAdmin):
    pass


@admin.register(models.BlogCategory)
class AdminBlogCategory(admin.ModelAdmin):
    pass


@admin.register(models.BlogComment)
class AdminBlogComment(admin.ModelAdmin):
    pass


@admin.register(models.Blog)
class AdminBlog(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title_in_url',)}
    list_display = ['title', 'auther', 'date_created', 'is_active', 'slug']
    fields = ['title', 'title_in_url', 'is_active', 'short_description', 'description',
              'image', 'tags', 'blog_categories', 'slug']
    exclude = ['auther', 'date_created', 'view_counter']

    def save_model(self, request, obj, form, change):
        obj.auther = request.user
        super().save_model(request, obj, form, change)
