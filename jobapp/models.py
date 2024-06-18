from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField

from mtaa import tanzania

User = get_user_model()

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

CATEGORY_TYPE = {
    ("In-Office", "In-Office"),
    ("Remote", "Remote"),
    ("Hybrid", "Hybrid"),
}

MARITAL_STATUS = {
    ("Single", "Single"),
    ("Married", "Married"),
    ("Widowed", "Widowed"),
}


class Category(models.Model):
    objects = models.Manager()
    # name = models.CharField(max_length=50)
    name = models.CharField(choices=CATEGORY_TYPE, max_length=50)
    # job_type = models.CharField(choices=JOB_TYPE, max_length=1)

    def __str__(self):
        return self.name


class Job(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE)
    image = CloudinaryField("image")
    title = models.CharField(max_length=300)
    description = RichTextField()
    tags = TaggableManager()
    location = models.CharField(choices=[(loc, loc) for loc in tanzania], max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    category = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=300)
    company_description = RichTextField(blank=True, null=True)
    url = models.URLField(max_length=200)
    employee_age = models.IntegerField(default=0, blank=True, null=True)
    # employee_relevance_score = models.FloatField(default=0, blank=True, null=True)
    last_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JobSkills(models.Model):
    objects = models.Manager()
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="jobskills")
    skill = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"The skills required for {self.job}"


class RecommendedApplicant(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    relevance = models.FloatField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.job.title


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    relevance = models.FloatField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.job.title


class BookmarkJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.job.title


class Candidate(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidate')
    image = CloudinaryField("image")
    age = models.IntegerField(null=True, blank=True)
    place_of_birth = models.CharField(choices=[(loc, loc) for loc in tanzania], max_length=300, default="Tabora")
    place_of_domicile = models.CharField(choices=[(loc, loc) for loc in tanzania], max_length=300, default="Tabora")
    nationality = models.CharField(max_length=300, blank=True, null=True, default="Nationality")
    marital_status = models.CharField(choices=MARITAL_STATUS, max_length=50, default="Single")
    language = models.CharField(max_length=300, blank=True, null=True, default="Marital")
    university_level = models.CharField(max_length=300, blank=True, null=True, default="University of Dodoma")
    advanced_level = models.CharField(max_length=300, blank=True, null=True, default="Tabora Boys High School")
    ordinary_level = models.CharField(max_length=300, blank=True, null=True, default="Alliance Boys Secondary School")
    primary_level = models.CharField(max_length=300, blank=True, null=True, default="St. Francis De Sales Mission School")
    company = models.CharField(max_length=300, blank=True, null=True)
    position = models.CharField(max_length=300, blank=True, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    duties = models.CharField(max_length=300, blank=True, null=True)
    hobbies = models.CharField(max_length=300, blank=True, null=True)
    reason_for_leaving = models.CharField(max_length=300, null=True, blank=True)
    # location = models.CharField(choices=[(loc, loc) for loc in tanzania], max_length=300)
    skills = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user}"


class MatchResult(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(Job, on_delete=models.CASCADE)
    relevance_score = models.FloatField()
