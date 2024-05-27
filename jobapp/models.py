from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

User = get_user_model()

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

CATEGORY_TYPE = {
    ()
}


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = RichTextField()
    tags = TaggableManager()
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    category = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=300)
    company_description = RichTextField(blank=True, null=True)
    url = models.URLField(max_length=200)
    employee_age = models.IntegerField(default=0, blank=True, null=True)
    employee_relevance_score = models.FloatField(default=0, blank=True, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    skills = models.CharField(max_length=300, blank=False, null=False)
    education = models.CharField(max_length=300, blank=False, null=False)
    work_experience = models.CharField(max_length=300, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.user}"


class MatchResult(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(Job, on_delete=models.CASCADE)
    relevance_score = models.FloatField()
