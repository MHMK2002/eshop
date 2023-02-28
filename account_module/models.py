from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='files/images',
                              verbose_name='پروفایل کاربر',
                              default='medias/images/default-profile.png')
    phone_number = models.CharField(max_length=20, verbose_name='تلفن همراه', null=True)
    email_activation_code = models.CharField(max_length=300, verbose_name='کد فعال سازی', null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

