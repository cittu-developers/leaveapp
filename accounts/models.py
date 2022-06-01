from django.db import models
from django.contrib.auth.models import AbstractUser
from registry.models import *
# Create your models here.

class Gender(models.Model):
    title = models.CharField(blank=True,null=True,max_length=10)

    def __str__(self):
        return self.title
class Country(models.Model):
    title = models.CharField(blank=True,null=True,max_length=10)

    def __str__(self):
        return self.title

class Directorate(models.Model):
    title = models.CharField(max_length=50)
  
    def __str__(self):
        return self.title
class Department(models.Model):
    title = models.CharField(max_length=50)
    directorate = models.ForeignKey(Directorate, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title

class Unit(models.Model):
    title = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title

class SubUnit(models.Model):
    title = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title

class User(AbstractUser):
    first_name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    other_name = models.CharField(max_length=50)
    file_number = models.IntegerField(default=0, unique=True, )
    username = models.CharField(unique=True, max_length=30)
    date_of_birth = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE,null=True,blank=True)
    nationality =models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True)
    directorate = models.ForeignKey(Directorate, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True,blank=True)
    sub_unit = models.ForeignKey(SubUnit, on_delete=models.CASCADE,null=True,blank=True)
    passport = models.ImageField(upload_to='passport', null=True, blank=True, default="default.jpg")
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name','last_name','other_name','file_number','date_of_birth','gender','nationality','directorate','department')

    def __str__(self):
        return str(self.username)