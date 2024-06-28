import random

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Job, JobSkills, RecommendedApplicant, Candidate
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
                   f"Give the answer in percentage without any words whatsoever, no negative percentage!, "
                   f"Percent starts from 50 onwards")
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
        # obj.age = Candidate.objects.get(user__id=user_pk).age
        # obj.relevance = random.randint(50, 100)
        # obj.save()
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
            obj = RecommendedApplicant.objects.get_or_create(user_id=user_pk, job_id=job_id)
            obj[0].age = age
            obj[0].relevance = random.randint(50, 100)
            obj[0].save()

            to_send = User.objects.get(id=user_pk)
            full_name = f"{to_send.first_name} {to_send.last_name}"
            email = to_send.email
            subject = 'JobLink Recommendation System Alert'
            message = (f'Dear {full_name}, you have been Recommended to this Job {job.title} from '
                       f'{job.company_name} Company. \n\nYou can also apply to increase your chances of getting the Job!')
            from_email = 'no-reply-akacha@raxan7.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            # relevance = calculate_percentage_relevance(need_age=job.employee_age, need_position=job.title,
            #                                            need_skill=i.skill,
            #                                            have_age=age, have_skill=list_of_skills)

            # relevance = int(relevance)
            # old_relevance = 0
            # if relevance == 0:
            #     relevance = 50
            #     obj = RecommendedApplicant.objects.get_or_create(user_id=user_pk, job_id=job_id)
            #     obj[0].age = age
            #     obj[0].relevance = relevance
            #     obj[0].save()
            # else:
            #     if relevance < old_relevance:
            #         pass
            #     elif relevance > old_relevance:
            #         if relevance == 100:
            #             relevance = - 10
            #             obj = RecommendedApplicant.objects.get_or_create(user_id=user_pk, job_id=job_id)
            #             obj[0].age = age
            #             obj[0].relevance = relevance
            #             obj[0].save()
            #             old_relevance = relevance

    return JsonResponse({'message': 'Applicants recommended for the job successfully.'})
# from django.core.mail import send_mail
# from django.shortcuts import get_object_or_404, render
# from django.http import JsonResponse
# from .models import Job, JobSkills, RecommendedApplicant
# from app.models import add_skill
# from django.contrib.auth import get_user_model
# import google.generativeai as genai
# from django.db import IntegrityError, transaction
#
# from transformers import BertTokenizer, BertModel
# from sklearn.metrics.pairwise import cosine_similarity
#
# GOOGLE_API_KEY = 'AIzaSyAX8YiDkmNyeLhCnGZOZ4Uq_2gJyXvatNs'
# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel('gemini-pro')
#
# User = get_user_model()
#
# # Load pre-trained BERT model and tokenizer
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# pre_trained_model = BertModel.from_pretrained('bert-base-uncased')
#
#
# def get_bert_embeddings(text):
#     inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding=True)
#     outputs = pre_trained_model(**inputs)
#     return outputs.last_hidden_state.mean(dim=1).detach().numpy()
#
#
# def calculate_relevance_score(context1, context2):
#     emb1 = get_bert_embeddings(context1)
#     emb2 = get_bert_embeddings(context2)
#     similarity = cosine_similarity(emb1, emb2)[0][0]
#     return similarity * 100  # Convert to percentage
#
#
# def calculate_percentage_relevance(need_age, need_position, need_skill, have_age, have_skill):
#     employer = f"I want a {need_age} yrs old {need_position} who is well equipped in {need_skill}"
#     employee = f"I am {have_age} yrs old and i am well equipped in {have_skill}"
#     response = calculate_relevance_score(employer, employee)
#     response = round(response, 2)
#     return response
#
#
# # 1. Automatically recommending applicants when a job is created
# def recommend_applicants_for_job(request, job_id):
#     job = get_object_or_404(Job, pk=job_id)
#     job_skills = job.jobskills.values_list('skill', flat=True)
#     print(job_skills)
#     users_with_skills = add_skill.objects.filter(name__in=job_skills).values_list('email', flat=True)
#     print(users_with_skills)
#     for user_id in users_with_skills:
#         user_pk = User.objects.get(email=user_id).id
#         RecommendedApplicant.objects.get_or_create(user_id=user_pk, job_id=job_id)
#     return JsonResponse({'message': 'Applicants recommended for the job successfully.'})
#
#
# # 1. Automatically recommending applicants when a job is created
# def recommend_applicants_for_job_with_relevance(request, list_of_skills, age):
#     print(f"The skills here are {list_of_skills}")
#
#     # Retrieve jobs that need the specified skills
#     jobs_needing = JobSkills.objects.filter(skill__in=list_of_skills).values_list('job', flat=True)
#     print(jobs_needing)
#
#     user_pk = request.user.id
#
#     for job_id in jobs_needing:
#         try:
#             job = Job.objects.get(id=job_id)
#
#             for skill in JobSkills.objects.filter(job=job):
#                 with transaction.atomic():
#                     # Use get_or_create with defaults to ensure unique creation or update
#                     obj, created = RecommendedApplicant.objects.get_or_create(
#                         user_id=user_pk,
#                         job_id=job_id,
#                         defaults={'age': age,
#                                   'relevance': calculate_percentage_relevance(need_age=job.employee_age,
#                                                                               need_position=job.title,
#                                                                               need_skill=skill.skill,
#                                                                               have_age=age,
#                                                                               have_skill=list_of_skills)}
#                     )
#
#                     # If the object already exists, update its fields
#                     if not created:
#                         obj.age = age
#                         obj.relevance = calculate_percentage_relevance(need_age=job.employee_age,
#                                                                        need_position=job.title,
#                                                                        need_skill=skill.skill,
#                                                                        have_age=age,
#                                                                        have_skill=list_of_skills)
#                         obj.save()
#                 to_send = User.objects.get(id=user_pk)
#                 full_name = f"{to_send.first_name} {to_send.last_name}"
#                 email = to_send.email
#                 subject = 'JobLink Recommendation System Alert'
#                 message = (f'Dear {full_name}, you have been Recommended to this Job {job.title} from '
#                            f'{job.company_name} Company. \n\nYou can also apply to increase your chances of getting the Job!')
#                 from_email = 'no-reply-akacha@raxan7.com'
#                 recipient_list = [email]
#                 send_mail(subject, message, from_email, recipient_list)
#
#         # except Job.DoesNotExist:
#         #     print(f"Job with id {job_id} does not exist.")
#         except IntegrityError:
#             print(f"Integrity error occurred for job id {job_id} and user id {user_pk}.")
