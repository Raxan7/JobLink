from django.db import transaction
from textblob import TextBlob
import re

from jobapp.models import *

# List of skills
skills_list = [
    "python", "java", "c++", "javascript", "php", "ruby", "swift", "kotlin",
    "html", "css", "react", "angular", "vue.js", "node.js", "express.js",
    "django", "flask", "spring", "ruby on rails", "asp.net", "jquery",
    "sql", "mysql", "postgresql", "mongodb", "firebase", "oracle",
    "machine learning", "deep learning", "data science", "data analysis",
    "artificial intelligence", "natural language processing",
    "computer vision", "big data", "blockchain", "cloud computing",
    "devops", "ci/cd", "docker", "kubernetes", "aws", "azure", "google cloud",
    "linux", "unix", "windows", "shell scripting", "bash", "powershell",
    "git", "github", "bitbucket", "jira", "trello", "slack", "confluence",
    "agile methodologies", "scrum", "kanban", "waterfall",
    "software development", "web development", "mobile app development",
    "game development", "ui/ux design", "graphic design", "illustration",
    "animation", "video editing", "motion graphics", "photography",
    "content writing", "copywriting", "technical writing", "blogging",
    "seo", "sem", "social media marketing", "email marketing",
    "sales", "marketing", "business development", "customer service",
    "project management", "product management", "quality assurance",
    "test automation", "manual testing", "continuous integration",
    "leadership", "problem solving", "critical thinking",
    "communication", "teamwork", "time management", "adaptability"
]


def insert_into_db(job_instance, skills_list):
    try:
        job_instance = Job.objects.get(id=job_instance)  # Replace with your job instance
        print("Job Instance:", job_instance)
        print("Skills List:", skills_list)

        job_skills_to_insert = [
            JobSkills(job=job_instance, skill=skill) for skill in skills_list
        ]

        with transaction.atomic():
            created_job_skills = JobSkills.objects.bulk_create(job_skills_to_insert)

        print("Number of created job skills:", len(created_job_skills))
        print("Bulk insertion successful.")
    except Exception as e:
        print("Error:", e)




def extract_skills_textblob(text):
    extracted_skills = []
    # Convert the text to lowercase for case-insensitive matching
    text_lower = text.lower()
    # Iterate over each skill in the skills list
    for skill in skills_list:
        # Construct a regular expression pattern for the skill (case-insensitive)
        pattern = re.compile(r'\b{}\b'.format(re.escape(skill)), re.IGNORECASE)
        # Check if the pattern matches in the text
        if pattern.search(text_lower):
            extracted_skills.append(skill)
    return extracted_skills
