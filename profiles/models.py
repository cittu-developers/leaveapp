from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gender(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=6)

    def __str__(self):
        return self.title


class Country(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title



class Biodata(models.Model):
    file_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.ForeignKey(Gender ,default=1, on_delete=models.CASCADE)
    nationality = models.ForeignKey(Country ,default='', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    passport = models.ImageField(null=True, blank=True, default="default.jpg")

    def __str__(self):
        return str(self.first_name)


    @property
    def imageURL(self):

        try:
            img = self.passport.url
        except:

            img = ''
        return img     




class SalaryScale(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title



class Directorate(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Signatory(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
            

class Department(models.Model):
    title = models.CharField(max_length=50)
    directorate = models.ForeignKey(Directorate, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Unit(models.Model):
    title = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SubUnit(models.Model):
    title = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title        


class EmploymentDetails(models.Model):
    biodata = models.ForeignKey(Biodata, on_delete=models.CASCADE)
    ministry = models.CharField(max_length=100)
    directorate = models.ForeignKey(Directorate, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    salary_scale = models.ForeignKey(SalaryScale, on_delete=models.CASCADE)
    grade = models.IntegerField()
    step = models.IntegerField()
    ippis_no = models.IntegerField(unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.biodata

