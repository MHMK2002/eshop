# Generated by Django 4.1.7 on 2023-02-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='موضوع')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('name', models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')),
                ('email', models.CharField(max_length=300, verbose_name='ایمیل')),
                ('response', models.TextField(null=True, verbose_name='پاسخ تماس با ما')),
                ('read_by_admin', models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس های با ما',
            },
        ),
    ]
