from django.contrib import admin
from .models import ContactUs


# Register your models here.
@admin.register(ContactUs)
class ContactUsModel(admin.ModelAdmin):
    list_display = ['title', 'name', 'email', 'message', 'read_by_admin', 'response', 'date']
    readonly_fields = ('date',)
