from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from jobapp.models import Job, JobSkills, RecommendedApplicant
from app.models import add_skill
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()

# 1. Automatically recommending applicants when a job is created
def recommend_applicants_for_job(request, list_of_skills):
    print(f"The skills here are {list_of_skills}")
    jobs_needing = JobSkills.objects.filter(skill__in=list_of_skills).values_list('job', flat=True)
    print(jobs_needing)
    for job_id in jobs_needing:
        user_pk = request.user.id
        print(user_pk)
        print(job_id)
        RecommendedApplicant.objects.get_or_create(user_id=user_pk, job_id=job_id)
    return JsonResponse({'message': 'Applicants recommended for the job successfully.'})
