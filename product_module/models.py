from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


class ProductTag(models.Model):
    tag = models.CharField(max_length=50, verbose_name='عنوان تگ')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.tag


class ProductCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی های محصولات'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(null=False, max_length=50, verbose_name='عنوان محصول')
    price = models.IntegerField(null=False, verbose_name='قیمت', validators=[MinValueValidator(0)])
    short_description = models.CharField(null=False, verbose_name='توضیحات کوتاه', max_length=200)
    description = models.TextField(verbose_name='توضیحات', max_length=2000)
    rating = models.IntegerField(verbose_name='امتیاز', validators=[MinValueValidator(1), MaxValueValidator(5)],
                                 default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=False, verbose_name='دسته بندی محصول')
    tags = models.ManyToManyField(ProductTag, verbose_name='تگ های محصول')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/غیرحذف شده')
    slug = models.SlugField(null=False, auto_created=True, verbose_name='اسلاگ', unique=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title
