from django.db import models


# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    url_title = models.CharField(verbose_name='عنوان لینک', max_length=200)
    url = models.URLField(verbose_name='لینک', max_length=500)
    image = models.ImageField(upload_to='files/images/slider', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='قعال / غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال بودن')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='آدرس')
    box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title
