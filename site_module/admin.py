from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass
