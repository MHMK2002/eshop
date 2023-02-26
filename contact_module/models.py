from django.db import models


# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='موضوع', null=False)
    message = models.TextField(verbose_name='متن پیام', null=False)
    name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی', null=False)
    date = models.DateTimeField(verbose_name='زمان ارسال', auto_now_add=True, auto_created=True)
    email = models.CharField(max_length=300, verbose_name='ایمیل', null=False)
    response = models.TextField(verbose_name='پاسخ تماس با ما', null=True)
    read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس های با ما'

    def __str__(self):
        return self.title
