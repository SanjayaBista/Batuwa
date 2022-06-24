from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Skill(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

Gender_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
  )
class Customer(models.Model):
    user_name = models.CharField(max_length = 40)
    email = models.EmailField()
    gender = models.CharField(max_length=40,choices=Gender_CHOICES)
    display_name = models.CharField(max_length=40)
    tagline = models.CharField(max_length=30)
    contact_number = models.IntegerField()
    language = models.CharField(max_length=30)
    image =  models.ImageField(upload_to ='images/')
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    customer = models.OneToOneField(User, on_delete = models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.userName


class Address(models.Model):
    state = models.CharField(max_length=20)
    zipCode = models.IntegerField()
    country = CountryField()
    address = models.CharField(max_length=50)
    customer_address = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.address


class SocialLinks(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    linkedlin = models.URLField()
    behance = models.URLField()
    dribble = models.URLField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE,blank=True, null=True)

class Project(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category



PRICETYPE_CHOICES = (
    ('HOURLY RATE', 'HOURLY RATE'),
    ('HALF DAY RATE', 'HALF DAY RATE'),
    ('FULL DAY RATE', 'FULL DAY RATE')
)

PERIOD_OF_PROJECT = [
    ('START_IMMEDIATE','SI'),
    ('JOB_DATE','JD'),
]

PROJECT_STATUS = [
    ('Active','active'),
    ('Inactive','inactive'),
    ('Trash','trash')
]
class ProjectDetail(models.Model):
    title = models.CharField(max_length=100)
    price_type = models.CharField(max_length=40, choices = PRICETYPE_CHOICES, default="HOURLY RATE")
    location = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    addedOn = models.DateTimeField(auto_now_add = True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    expertise = models.ManyToManyField(Skill, blank=True)
    project_period = models.CharField(max_length=250,blank=True,choices=PERIOD_OF_PROJECT)
    start_date = models.DateField(auto_now_add=False,blank=True,null=True)
    is_start_immediately = models.BooleanField(default=False)
    end_date = models.DateField( auto_now=False, auto_now_add=False,blank=True,null=True)
    document = models.FileField(upload_to="verification/", null=True, blank=True)
    links = models.URLField(null=True, blank=True)
    description = models.TextField()
    price = models.FloatField(null=True, blank=True)
    project_status  = models.CharField(max_length=40, choices = PROJECT_STATUS, default="Active")
    technology = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('Freelancing:view_project_detail',args=[self.id])
    
    # @property
    # def project_days(self):
    #     given_date = self.addedOn
    #     due_date = self.end_date
    #     expire = givenDate - due_date
    #     return expire.days
    
    # @property
    # def remaining_days(self):
    #     today_date = date.today()
    #     due_date = self.end_date
    #     remaining = due_date - today_date
    #     return remaining.days

class Review(models.Model):
    title = models.CharField(max_length=40)
    rating = models.IntegerField()
    description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True, null=True)
    

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=40)
    link = models.URLField()
    files = models.FileField(upload_to="Files/")
    description = models.TextField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title
class Verificaion(models.Model):
    your_name = models.CharField(max_length=30)
    contact_number = models.IntegerField()
    passport = models.CharField(max_length=30)
    document = models.FileField(upload_to= "verification/")
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    address  = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.yourName


class Blog(models.Model):
    image = models.ImageField(upload_to="images/")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


