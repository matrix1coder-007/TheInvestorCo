# Generated by Django 4.2.1 on 2023-06-20 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusermodel',
            name='user_registration_auth_code',
        ),
        migrations.RemoveField(
            model_name='customusermodel',
            name='user_registration_email_sent',
        ),
    ]