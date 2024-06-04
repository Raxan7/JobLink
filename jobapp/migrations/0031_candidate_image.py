# Generated by Django 3.2.16 on 2024-06-03 19:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0030_remove_job_employee_relevance_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='image',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]