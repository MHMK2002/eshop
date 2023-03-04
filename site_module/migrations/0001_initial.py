# Generated by Django 4.1.7 on 2023-03-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام سایت')),
                ('logo', models.ImageField(upload_to='files/images/site-settings/', verbose_name='لوگو')),
                ('about_us_module', models.TextField(verbose_name='درباره ما')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='تلفن')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('telegram', models.CharField(blank=True, max_length=200, null=True, verbose_name='تلگرام')),
                ('instagram', models.CharField(blank=True, max_length=200, null=True, verbose_name='اینستاگرام')),
                ('twitter', models.CharField(blank=True, max_length=200, null=True, verbose_name='توییتر')),
                ('fax', models.CharField(blank=True, max_length=20, null=True, verbose_name='فکس')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='آدرس سایت')),
                ('mail_setting', models.BooleanField(default=False, verbose_name='تنظیمات اصلی')),
                ('copy_right', models.TextField(verbose_name='کپی رایت')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
    ]