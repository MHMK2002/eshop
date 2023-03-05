from django.contrib import admin
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
    prepopulated_fields = {'slug': ('title',)}
