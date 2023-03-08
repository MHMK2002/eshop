from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='files/images',
                              verbose_name='پروفایل کاربر',
                              default='medias/images/default-profile.png')
    phone_number = models.CharField(max_length=20, verbose_name='تلفن همراه', null=True)
    email_activation_code = models.CharField(max_length=100, verbose_name='کد فعال سازی', null=True)
    password_activation_code = models.CharField(max_length=100, verbose_name='کد فعال سازی رمز عبور', null=True)

    def __str__(self):
        if self.get_full_name() is not '':
            return self.get_full_name()
        else:
            return self.get_username()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

