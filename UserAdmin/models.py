from itertools import count
from django.db import models 

# Create your models here.
class Website(models.Model):
    website_name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='websiteLogo',null=True, blank=True)
    favicon = models.ImageField(upload_to='websiteFavicon', blank=True, null=True)

    def __str__(self):
        return self.website_name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.city