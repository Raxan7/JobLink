# Generated by Django 5.0.6 on 2024-06-18 02:21

import ckeditor.fields
import cloudinary.models
import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Hybrid', 'Hybrid'), ('In-Office', 'In-Office'), ('Remote', 'Remote')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('place_of_birth', models.CharField(choices=[('Shinyanga', 'Shinyanga'), ('Mara', 'Mara'), ('Dar-es-salaam', 'Dar-es-salaam'), ('Kilimanjaro', 'Kilimanjaro'), ('Kagera', 'Kagera'), ('Tanga', 'Tanga'), ('Mwanza', 'Mwanza'), ('Tabora', 'Tabora'), ('Kigoma', 'Kigoma'), ('Pwani', 'Pwani'), ('Ruvuma', 'Ruvuma'), ('Mtwara', 'Mtwara'), ('Morogoro', 'Morogoro'), ('Rukwa', 'Rukwa'), ('Katavi', 'Katavi'), ('Simiyu', 'Simiyu'), ('Geita', 'Geita'), ('Arusha', 'Arusha'), ('Iringa', 'Iringa'), ('Mbeya', 'Mbeya'), ('Njombe', 'Njombe'), ('Manyara', 'Manyara'), ('Lindi', 'Lindi'), ('Singida', 'Singida'), ('Songwe', 'Songwe'), ('Dodoma', 'Dodoma')], max_length=300)),
                ('place_of_domicile', models.CharField(choices=[('Shinyanga', 'Shinyanga'), ('Mara', 'Mara'), ('Dar-es-salaam', 'Dar-es-salaam'), ('Kilimanjaro', 'Kilimanjaro'), ('Kagera', 'Kagera'), ('Tanga', 'Tanga'), ('Mwanza', 'Mwanza'), ('Tabora', 'Tabora'), ('Kigoma', 'Kigoma'), ('Pwani', 'Pwani'), ('Ruvuma', 'Ruvuma'), ('Mtwara', 'Mtwara'), ('Morogoro', 'Morogoro'), ('Rukwa', 'Rukwa'), ('Katavi', 'Katavi'), ('Simiyu', 'Simiyu'), ('Geita', 'Geita'), ('Arusha', 'Arusha'), ('Iringa', 'Iringa'), ('Mbeya', 'Mbeya'), ('Njombe', 'Njombe'), ('Manyara', 'Manyara'), ('Lindi', 'Lindi'), ('Singida', 'Singida'), ('Songwe', 'Songwe'), ('Dodoma', 'Dodoma')], max_length=300)),
                ('nationality', models.CharField(blank=True, default='Nationality', max_length=300, null=True)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Widowed', 'Widowed')], default='Single', max_length=50)),
                ('language', models.CharField(blank=True, default='Marital', max_length=300, null=True)),
                ('university_level', models.CharField(blank=True, default='University of Dodoma', max_length=300, null=True)),
                ('advanced_level', models.CharField(blank=True, default='Tabora Boys High School', max_length=300, null=True)),
                ('ordinary_level', models.CharField(blank=True, default='Alliance Boys Secondary School', max_length=300, null=True)),
                ('primary_level', models.CharField(blank=True, default='St. Francis De Sales Mission School', max_length=300, null=True)),
                ('company', models.CharField(blank=True, max_length=300, null=True)),
                ('position', models.CharField(blank=True, max_length=300, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('duties', models.CharField(blank=True, max_length=300, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=300, null=True)),
                ('reason_for_leaving', models.CharField(blank=True, max_length=300, null=True)),
                ('skills', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=300)),
                ('description', ckeditor.fields.RichTextField()),
                ('location', models.CharField(choices=[('Shinyanga', 'Shinyanga'), ('Mara', 'Mara'), ('Dar-es-salaam', 'Dar-es-salaam'), ('Kilimanjaro', 'Kilimanjaro'), ('Kagera', 'Kagera'), ('Tanga', 'Tanga'), ('Mwanza', 'Mwanza'), ('Tabora', 'Tabora'), ('Kigoma', 'Kigoma'), ('Pwani', 'Pwani'), ('Ruvuma', 'Ruvuma'), ('Mtwara', 'Mtwara'), ('Morogoro', 'Morogoro'), ('Rukwa', 'Rukwa'), ('Katavi', 'Katavi'), ('Simiyu', 'Simiyu'), ('Geita', 'Geita'), ('Arusha', 'Arusha'), ('Iringa', 'Iringa'), ('Mbeya', 'Mbeya'), ('Njombe', 'Njombe'), ('Manyara', 'Manyara'), ('Lindi', 'Lindi'), ('Singida', 'Singida'), ('Songwe', 'Songwe'), ('Dodoma', 'Dodoma')], max_length=300)),
                ('job_type', models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=1)),
                ('salary', models.CharField(blank=True, max_length=30)),
                ('company_name', models.CharField(max_length=300)),
                ('company_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('url', models.URLField()),
                ('employee_age', models.IntegerField(blank=True, default=0, null=True)),
                ('last_date', models.DateField()),
                ('is_published', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='jobapp.category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookmarkJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.job')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relevance', models.FloatField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.job')),
            ],
        ),
        migrations.CreateModel(
            name='JobSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(blank=True, max_length=200, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobskills', to='jobapp.job')),
            ],
        ),
        migrations.CreateModel(
            name='MatchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relevance_score', models.FloatField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.candidate')),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.job')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendedApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relevance', models.FloatField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobapp.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
