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

