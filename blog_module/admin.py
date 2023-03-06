from django.contrib import admin
from django.http import HttpRequest

from account_module.models import User
from . import models


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
    list_display = ['auther', 'title']
    exclude = ['auther']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.auther = request.user
        super().save_model(request, obj, form, change)
