# Generated by Django 4.2.4 on 2025-01-12 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('gender', models.TextField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('address', models.CharField(blank=True, max_length=80)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_patient', models.BooleanField(default=True, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('residence_address', models.CharField(blank=True, max_length=100)),
                ('registration_address', models.CharField(blank=True, max_length=100)),
                ('room_name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('license_number', models.CharField(max_length=20, unique=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('contact_person_name', models.CharField(max_length=100)),
                ('contact_person_phone', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
        ),
    ]