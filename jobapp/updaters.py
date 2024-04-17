from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Job, JobSkills, RecommendedApplicant
from app.models import add_skill
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()

# 1. Automatically recommending applicants when a job is created
def recommend_applicants_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job_skills = job.jobskills.values_list('skill', flat=True)
    print(job_skills)
    users_with_skills = add_skill.objects.filter(name__in=job_skills).values_list('email', flat=True)
    print(users_with_skills)
    for user_id in users_with_skills:
        user_pk = User.objects.get(email=user_id).id
        RecommendedApplicant.objects.get_or_create(user_id=user_pk, job_id=job_id)
    return JsonResponse({'message': 'Applicants recommended for the job successfully.'})


def populate_recommended_applicant(request):
    # Get data from the request
    email = request.POST.get('email')
    extracted_skills = request.POST.getlist('skills')

    # Get users with the provided email and extracted skills
    users_with_skills = add_skill.objects.filter(email=email, name__in=extracted_skills)

    # Get job IDs that require the skills of the registering user
    job_ids_with_matching_skills = JobSkills.objects.filter(skill__in=extracted_skills).values_list('job_id', flat=True)

    # Iterate over users with skills and create RecommendedApplicant instances
    for user_with_skills in users_with_skills:
        for job_id in job_ids_with_matching_skills:
            RecommendedApplicant.objects.get_or_create(user=user_with_skills.user, job_id=job_id)

    # Return success response
    return JsonResponse({'message': 'Recommended applicants updated successfully.'})


