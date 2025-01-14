# Generated by Django 4.2.1 on 2023-06-18 14:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='pkey_user')),
                ('user_fname', models.CharField(max_length=100, verbose_name='First Name')),
                ('user_mname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle Name')),
                ('user_lname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name')),
                ('user_email', models.EmailField(max_length=200, unique=True, verbose_name='User Registration E-Mail')),
                ('user_registration_email_sent', models.BooleanField(default=False, verbose_name='Registration E-Mail check')),
                ('user_registration_auth_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Registration Auth-Code')),
                ('user_registered', models.BooleanField(default=True, verbose_name='Is Active')),
                ('user_deactivation_dt', models.DateTimeField(blank=True, null=True, verbose_name='Deactivation Date')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Custom User',
                'verbose_name_plural': 'Custom Users',
                'db_table': 'Custom_User',
                'abstract': False,
            },
        ),
    ]
