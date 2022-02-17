from django.db import models

# Create your models here.

class Ecom_Armchairs(models.Model):

    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    discount=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(default="null")

class Ecom_Dining(models.Model):

    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    discount=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(default="null")

class Ecom_Bed(models.Model):

    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    discount=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(default="null")

class Ecom_Chair(models.Model):

    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    discount=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(default='null')

class Customer_Reg(models.Model):

    name=models.CharField(max_length=200)
    age=models.CharField(max_length= 200)
    address=models.CharField(max_length= 200)
    phone=models.CharField(max_length=200)
    account = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class Admin_Reg(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
