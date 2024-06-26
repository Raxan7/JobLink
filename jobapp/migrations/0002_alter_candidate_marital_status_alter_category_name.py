# Generated by Django 5.0.6 on 2024-06-18 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed')], default='Single', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('In-Office', 'In-Office'), ('Remote', 'Remote'), ('Hybrid', 'Hybrid')], max_length=50),
        ),
    ]
