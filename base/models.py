from django.db import models
from django.contrib import admin

class Address(models.Model):
    address1 = models.CharField(max_length=250, null=True, blank=True)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    address3 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.BigIntegerField(null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    address_type = models.CharField(max_length=250, null=True, blank=True)

admin.site.register(Address)

