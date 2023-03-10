from django.http import HttpResponse

from account_module.models import User
from django.db import models

from my_method_module.my_slug import get_unique_slug


class BlogCategory(models.Model):
    parent = models.ForeignKey(to='BlogCategory', verbose_name='والد', null=True, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    title_url = models.CharField(max_length=200, verbose_name='عنوان در url', unique=True)

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقالات'

    def __str__(self):
        return self.title


class BlogTag(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان تگ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ مقاله'
        verbose_name_plural = 'تگ های مقالات'


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    title_in_url = models.CharField(max_length=300, verbose_name='عنوان مقاله در url')
    short_description = models.TextField(verbose_name='خلاصه مقاله')
    description = models.TextField(verbose_name='متن مقاله')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد مقاله', editable=False)
    view_counter = models.IntegerField(verbose_name='تعداد بازدیدها', default=0, editable=False)
    image = models.ImageField(verbose_name='تصویر مقاله', upload_to='files/images/blogs')
    slug = models.SlugField(verbose_name='اسلاگ', allow_unicode=True, auto_created=True, blank=True)
    tags = models.ManyToManyField(to=BlogTag, verbose_name='تگ ها', blank=True)
    blog_categories = models.ManyToManyField(to=BlogCategory, verbose_name='دسته بندی ها')
    auther = models.ForeignKey(to=User, verbose_name='نویسنده', on_delete=models.CASCADE, editable=False)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = get_unique_slug(self.id, self.title_in_url, Blog.objects)
        super().save(*args, **kwargs)

    def get_rating(self):
        if len(self.blogcomment_set.all()) > 0:
            sum_rating = sum(self.blogcomment_set.all())
            count = len(self.blogcomment_set.all())
            return float(sum_rating) / count
        else:
            return 3

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class BlogComment(models.Model):
    replay = models.ForeignKey(to='BlogComment', verbose_name='ریپلای به', on_delete=models.CASCADE, null=True,
                               blank=True)
    auther = models.ForeignKey(to=User, verbose_name='کاربر', on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='نمره', null=True)
    text = models.TextField(verbose_name='متن نظر')
    blog = models.ForeignKey(to=Blog, verbose_name='مقاله', on_delete=models.CASCADE)
    date_created = models.DateTimeField(verbose_name='تاریخ نظر', auto_now_add=True)

    def __str__(self):
        return f"""{self.auther.username} {self.id}"""

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرها'
