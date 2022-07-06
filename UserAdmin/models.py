from itertools import count
from msilib.schema import RadioButton
from turtle import title
from django.db import models 
from Freelancing.models import Customer

# Create your models here.
class Website(models.Model):
    website_name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='websiteLogo',null=True, blank=True)
    favicon = models.ImageField(upload_to='websiteFavicon', blank=True, null=True)
    user = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True, null=True)

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
    user = models.OneToOneField(Customer, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.city

class Localization(models.Model):
    TIMEZONE = (
       ('(UTC +5:45)Asia/Katmandu', '(UTC +5:45)Asia/Katmandu'),
       ('(UTC +5:30)India', '(UTC +5:30)India')
        
    )
    DATE_FORMAT = (
       ('15 May 2016', '15 May 2016'),
       ('15/05/2016', '15/05/2016'),
       ('15.05.2016', '15.05.2016'),
       ('15-05-2016', '15-05-2016'),
        
    )
    TIME_FORMAT = (
       ('12 Hours', '12 Hours'),
       ('24 Hours', '24 Hours')
        
    )
    CURRENCY_SYMBOL = (
       ('$', '$'),
       ('£', '£'),
       ('₹', '₹'),
    )
    timezone = models.CharField(max_length=100, choices=TIMEZONE, default='(UTC +5:45)Asia/Katmandu')
    date_format = models.CharField(max_length=100, choices=DATE_FORMAT, default='15 May 2016')
    time_format = models.CharField(max_length=100, choices=TIME_FORMAT, default='12 Hours')
    currency_symbol = models.CharField(max_length=10, choices=CURRENCY_SYMBOL, default='$')

    def __str__(self):
        return self.timezone

class PaypalPayment(models.Model):
    option = models.CharField(max_length=10)
    braintree_token_key = models.CharField(max_length=100)
    braintree_merchant_id = models.CharField(max_length=100)
    braintree_public_key = models.CharField(max_length=100)
    braintree_private_key = models.CharField(max_length=100)
    paypal_app_id = models.CharField(max_length=100)
    paypal_secret_key = models.CharField(max_length=100)
    user = models.OneToOneField(Customer, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.user.user_name

class StripePayment(models.Model):
    option = models.CharField(max_length=10)
    gateway_name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    rest_key = models.CharField(max_length=100)
    user = models.OneToOneField(Customer, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.user.user_name

class SeoSetting(models.Model):
    title = models.CharField(max_length=100)
    keyword = models.CharField(max_length=150)
    description = models.TextField()
    user = models.OneToOneField(Customer, on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.title
