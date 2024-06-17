from django import forms
# from mtaa import tanzania

from jobapp.models import *
from ckeditor.widgets import CKEditorWidget


class JobForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Job Title :"
        self.fields['location'].label = "Job Location :"
        self.fields['salary'].label = "Salary :"
        self.fields['description'].label = "Job Description :"
        self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Submission Deadline :"
        self.fields['company_name'].label = "Company Name :"
        self.fields['url'].label = "Website :"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Software Developer',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : Bangladesh',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': '$800 - $1200',
            }
        )
        self.fields['tags'].widget.attrs.update(
            {
                'placeholder': 'Use comma separated. eg: Python, JavaScript ',
            }
        )
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',

            }
        )
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Company Name',
            }
        )
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )

    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "image",
            "job_type",
            "category",
            "salary",
            "description",
            "tags",
            "last_date",
            "company_name",
            "company_description",
            "url",
            'employee_age',
        ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Service is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("category is required")
        return category

    def save(self, commit=True):
        job = super(JobForm, self).save(commit=False)
        if commit:
            job.save()
        return job


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['job']


class JobBookmarkForm(forms.ModelForm):
    class Meta:
        model = BookmarkJob
        fields = ['job']


class JobEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Job Title :"
        self.fields['location'].label = "Job Location :"
        self.fields['salary'].label = "Salary :"
        self.fields['description'].label = "Job Description :"
        # self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Dead Line :"
        self.fields['company_name'].label = "Company Name :"
        self.fields['url'].label = "Website :"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Software Developer',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : Bangladesh',
            }
        )
        self.fields['salary'].widget.attrs.update(
            {
                'placeholder': '$800 - $1200',
            }
        )
        # self.fields['tags'].widget.attrs.update(
        #     {
        #         'placeholder': 'Use comma separated. eg: Python, JavaScript ',
        #     }
        # )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
            }
        )
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'Company Name',
            }
        )
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )

        last_date = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Service Name',
            'class': 'datetimepicker1'
        }))

    class Meta:
        model = Job

        fields = [
            "title",
            "location",
            "job_type",
            "category",
            "salary",
            "description",
            "last_date",
            "company_name",
            "company_description",
            "url"
        ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Job Type is required")
        return job_type

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("Category is required")
        return category

    def save(self, commit=True):
        job = super(JobEditForm, self).save(commit=False)

        if commit:
            job.save()
        return job


class CandidateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        self.fields['skills'].widget.attrs.update(
            {
                'placeholder': 'Python3, Django, ...',
            }
        )
        self.fields['university_level'].widget.attrs.update(
            {
                'placeholder': 'University Institutions Attended',
            }
        )
        self.fields['work_experience'].widget.attrs.update(
            {
                'placeholder': 'Work Experience...',
            }
        )
        self.fields['reason_for_leaving'].widget.attrs.update(
            {
                'placeholder': 'I quit, I was fired, I did not like the job.....',
            }
        )
        self.fields['age'].widget.attrs.update(
            {
                'placeholder': 'Age',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'Place of Residence',
            }
        )

    class Meta:
        model = Candidate
        fields = ['image', 'age', 'place_of_birth', 'place_of_domicile', 'nationality', 'marital_status', 'language', 'university_level', 
        'advanced_level', 'ordinary_level', 'primary_level', 'company', 'position', 'start_date', 'end_date', 'duties', 'hobbies', 
        'reason_for_leaving', 'skills']

    def save(self, commit=True):
        candidate = super(CandidateForm, self).save(commit=False)

        if commit:
            candidate.save()
        return candidate
