# Generated by Django 4.1.7 on 2023-03-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_alter_user_options_user_password_activation_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_user',
            field=models.TextField(blank=True, null=True, verbose_name='درباره شخص'),
        ),
    ]