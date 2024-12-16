# Generated by Django 4.2.4 on 2024-12-16 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=122, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
