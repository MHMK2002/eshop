from django.db import models


# Create your models here.
class SiteSettings(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام سایت')
    logo = models.ImageField(upload_to='files/images/site-settings/', verbose_name='لوگو')
    about_us = models.TextField(verbose_name='درباره ما')
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='تلفن', null=True, blank=True)
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    telegram = models.CharField(max_length=200, verbose_name='تلگرام' , null=True, blank=True)
    instagram = models.CharField(max_length=200, verbose_name='اینستاگرام', null=True, blank=True)
    twitter = models.CharField(max_length=200, verbose_name='توییتر', null=True, blank=True)
    fax = models.CharField(max_length=20, verbose_name='فکس', null=True, blank=True)
    url = models.CharField(max_length=200, verbose_name='آدرس سایت', null=True, blank=True)
    mail_setting = models.BooleanField(default=False, verbose_name='تنظیمات اصلی')
    copy_right = models.TextField(verbose_name='کپی رایت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

