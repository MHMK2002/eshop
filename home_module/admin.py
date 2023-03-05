from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Slider)
class AdminSlider(admin.ModelAdmin):
    pass


@admin.register(models.FooterLinkBox)
class AdminFooterLinkBox(admin.ModelAdmin):
    pass


@admin.register(models.FooterLink)
class AdminFooterLink(admin.ModelAdmin):
    pass
