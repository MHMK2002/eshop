# Generated by Django 4.1.7 on 2023-03-06 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]