from ast import Str
from django.contrib import admin
from .models import Country, State, Address, Website, Localization, PaypalPayment, StripePayment, SeoSetting
# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Address)
admin.site.register(Website)
admin.site.register(Localization)
admin.site.register(PaypalPayment)
admin.site.register(StripePayment)
admin.site.register(SeoSetting)