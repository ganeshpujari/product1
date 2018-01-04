from django.db import models
from django.contrib import admin




class Shirts(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    pic=models.ImageField(upload_to='pics',null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    code=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    is_active=models.BooleanField(default=True)

admin.site.register(Shirts)

class Jeans(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    pic=models.ImageField(upload_to='pics',null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    code=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    is_active=models.BooleanField(default=True)

admin.site.register(Jeans)

class Jackets(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    pic=models.ImageField(upload_to='pics',null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    code=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    is_active=models.BooleanField(default=True)

admin.site.register(Jackets)

class Gymwear(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    pic=models.ImageField(upload_to='pics',null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    code=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    is_active=models.BooleanField(default=True)

admin.site.register(Gymwear)

class Watches(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    pic=models.ImageField(upload_to='pics',null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    code=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    is_active=models.BooleanField(default=True)

admin.site.register(Watches)

class Sunglasses(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    pic=models.ImageField(upload_to='pics',null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    code=models.CharField(max_length=150,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    is_active=models.BooleanField(default=True)

admin.site.register(Sunglasses)