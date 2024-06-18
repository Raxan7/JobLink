# Generated by Django 5.0.6 on 2024-06-18 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='marital_status',
            field=models.CharField(choices=[('Widowed', 'Widowed'), ('Single', 'Single'), ('Married', 'Married')], default='Single', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('In-Office', 'In-Office'), ('Hybrid', 'Hybrid'), ('Remote', 'Remote')], max_length=50),
        ),
    ]