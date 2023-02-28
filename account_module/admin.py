from django.contrib import admin

from account_module.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ['password']
