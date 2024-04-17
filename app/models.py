from django.db import models

# Create your models here.
#academic
class add_degree(models.Model):
	name=models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return self.name
class add_field_of_study(models.Model):
	name=models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return self.name
class academic(models.Model):
	name=models.CharField(max_length=200, null=True, blank=True)
	email=models.CharField(max_length=200, null=True, blank=True)
	school_or_college=models.CharField(max_length=200, null=True, blank=True)
	degree=models.ForeignKey(add_degree,on_delete=models.CASCADE,null=True,blank=True)
	field_of_study=models.ForeignKey(add_field_of_study,on_delete=models.CASCADE,null=True,blank=True)

	start_date=models.DateField()
	end_date=models.DateField(null=True,blank=True)
	grade=models.CharField(max_length=200,null=True,blank=True)
	def __str__(self):
		return self.name

SALARY_CHOICES = (
	    ('1,50,000','2,00,000'),
	    ('2,00,000','2,50,000'),
	    ('2,50,000','3,00,000'),
	    ('above 3,00,000','>3,00,000'),
	    
	)


#professional
EMP_TYPE_CHOICES = (
	    ('Internship','Internship'),
	    ('Full-time','Full-time'),
	    ('Part-time','Part-time'),
	    ('Self-employed','Self-employed'),
	    ('Freelance','Freelance'),
	    ('Contract','Contract')
	    )


class professional_pro(models.Model):
	name=models.CharField(max_length=200, null=True, blank=True)
	email=models.CharField(max_length=200, null=True, blank=True)
	title=models.CharField(max_length=400, null=True, blank=True)
	employment_type=models.CharField(max_length=200, choices=EMP_TYPE_CHOICES,default='Full-time')
	company=models.CharField(max_length=1000, null=True, blank=True)
	current_company=models.BooleanField()
	location=models.CharField(max_length=200, null=True, blank=True)
	start_date=models.DateField()
	end_date=models.DateField()
	description=models.CharField(max_length=500, null=True, blank=True)
	def __str__(self):
		return self.name
class add_project(models.Model):
	email=models.CharField(max_length=200, null=True, blank=True)
	project_name=models.CharField(max_length=200, null=True, blank=True)
	start_date=models.DateField()
	end_date=models.DateField()
	description=models.CharField(max_length=500, null=True, blank=True)
	project_url=models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return self.email
	
class add_skill(models.Model):
	email=models.CharField(max_length=200, null=True, blank=True)
	name=models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
        # Trim spaces from fields
		self.email = self.email.strip()
		self.name = self.name.strip()

        # Convert text to lowercase
		self.email = self.email.lower()
		self.name = self.name.lower()

        # Call the parent class's save method
		super(add_skill, self).save(*args, **kwargs)

class add_certifications(models.Model):
	email=models.CharField(max_length=200, null=True, blank=True)
	title=models.CharField(max_length=200, null=True, blank=True)
	organization=models.CharField(max_length=200, null=True, blank=True)
	issued_date=models.DateField()
	issued_id=models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return self.email



GENDER_CHOICES = (
	    ('MALE','MALE'),
	    ('FEMALE','FEMALE'),
	    
	)
MARITAL_CHOICES = (
	    ('MARRIED','MARRIED'),
	    ('UNMARRIED','UNMARRIED'),
	    
	)

CATEGORY_CHOICES = (
	    ('GENERAL','GENERAL'),
	    ('SC/ST','SC/ST'),
	    ('OBC','OBC')
	    
	)


#social
class social(models.Model):
	#name=models.CharField(max_length=200,null=True,blank=True)
	email=models.CharField(max_length=200, null=True, blank=True)
	dob=models.CharField(max_length=400, null=True, blank=True)
	gender=models.CharField(max_length=1000,choices=GENDER_CHOICES,default='MALE')
	martial=models.CharField(max_length=200, choices=MARITAL_CHOICES,default='MARRIED')
	hometown=models.CharField(max_length=500, null=True, blank=True)
	hobbies=models.CharField(max_length=500, null=True, blank=True)
	mobile_number=models.CharField(max_length=13,null=True,blank=True)
	#category=models.CharField(max_length=500,choices=CATEGORY_CHOICES,default='GENERAL')
	#languages=models.CharField(max_length=500, null=True, blank=True)
	linkedin_profile=models.CharField(max_length=500, null=True, blank=True)
	facebook_profile=models.CharField(max_length=500, null=True, blank=True)
	def __str__(self):
		return self.email