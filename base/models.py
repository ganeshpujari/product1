from django.db import models
from django.contrib import admin




class Shirts(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    pic=models.ImageField(upload_to='pics',null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    code=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

admin.site.register(Shirts)