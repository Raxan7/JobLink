# Generated by Django 5.0.6 on 2024-06-17 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0040_auto_20240610_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='education',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='work_experience',
            new_name='duties',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='location',
            new_name='place_of_birth',
        ),
        migrations.AddField(
            model_name='candidate',
            name='advanced_level',
            field=models.CharField(blank=True, default='Tabora Boys High School', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='hobbies',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='language',
            field=models.CharField(blank=True, default='Marital', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='marital_status',
            field=models.CharField(choices=[('Widowed', 'Widowed'), ('Married', 'Married'), ('Single', 'Single')], default='Single', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='nationality',
            field=models.CharField(blank=True, default='Nationality', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='ordinary_level',
            field=models.CharField(blank=True, default='Alliance Boys Secondary School', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='place_of_domicile',
            field=models.CharField(choices=[('Shinyanga', 'Shinyanga'), ('Mara', 'Mara'), ('Dar-es-salaam', 'Dar-es-salaam'), ('Kilimanjaro', 'Kilimanjaro'), ('Kagera', 'Kagera'), ('Tanga', 'Tanga'), ('Mwanza', 'Mwanza'), ('Tabora', 'Tabora'), ('Kigoma', 'Kigoma'), ('Pwani', 'Pwani'), ('Ruvuma', 'Ruvuma'), ('Mtwara', 'Mtwara'), ('Morogoro', 'Morogoro'), ('Rukwa', 'Rukwa'), ('Katavi', 'Katavi'), ('Simiyu', 'Simiyu'), ('Geita', 'Geita'), ('Arusha', 'Arusha'), ('Iringa', 'Iringa'), ('Mbeya', 'Mbeya'), ('Njombe', 'Njombe'), ('Manyara', 'Manyara'), ('Lindi', 'Lindi'), ('Singida', 'Singida'), ('Songwe', 'Songwe'), ('Dodoma', 'Dodoma')], default='Tabora', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='primary_level',
            field=models.CharField(blank=True, default='St. Francis De Sales Mission School', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='university_level',
            field=models.CharField(blank=True, default='University of Dodoma', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Hybrid', 'Hybrid'), ('Remote', 'Remote'), ('In-Office', 'In-Office')], max_length=50),
        ),
    ]