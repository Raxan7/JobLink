from ast import literal_eval

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Job, JobSkills, RecommendedApplicant
from app.models import add_skill
from django.db.models import Q
from django.contrib.auth import get_user_model
import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyAX8YiDkmNyeLhCnGZOZ4Uq_2gJyXvatNs'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

User = get_user_model()


def calculate_percentage_relevance(need_age, need_position, need_skill, have_age, have_skill):
    """
    I need to get the employee's relevance from the Candidate model's attributes, in comparison to the
    Job model's details
    """
    full_prompt = (f"Employer : I want a {need_age} yrs old {need_position} who is well equipped in {need_skill}"
                   f"Employee : I am {have_age} yrs old and i am well equipped in {have_skill}"
                   f"Can you rate in percentage the relevance of the Employee to the Employer ?"
                   f"Give the answer in percentage without any words whatsoever")
    response = model.generate_content(full_prompt)
    print(response.text)
    response = str(response.text)
    if response.endswith('%'):
        response = response[:-1]
    else:
        response = int(response)
    return response


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


# 1. Automatically recommending applicants when a job is created
def recommend_applicants_for_job_with_relevance(request, list_of_skills, age):
    print(f"The skills here are {list_of_skills}")
    jobs_needing = JobSkills.objects.filter(skill__in=list_of_skills).values_list('job', flat=True)
    print(jobs_needing)
    for job_id in jobs_needing:
        user_pk = request.user.id
        job = Job.objects.get(id=job_id)
        for i in JobSkills.objects.filter(job=job):
            relevance = calculate_percentage_relevance(need_age=job.employee_age, need_position=job.title,
                                                       need_skill=i.skill,
                                                       have_age=age, have_skill=list_of_skills)
            obj = RecommendedApplicant.objects.get_or_create(user_id=user_pk, job_id=job_id)
            obj[0].age = age
            obj[0].relevance = relevance
            obj[0].save()
    return JsonResponse({'message': 'Applicants recommended for the job successfully.'})
