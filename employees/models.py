from django.db import models

# Create your models here.


class Designation(models.Model):
    designation_name = models.CharField(max_length=100,unique=True)
    isauthorised = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.designation_name

class Department(models.Model):
    department_name = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.department_name

class Zonal(models.Model):
    zonal_name = models.CharField(max_length=150,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return  self.zonal_name


class Employee(models.Model):
    username = models.CharField(max_length=150,unique=True)
    name = models.CharField(max_length=150)
    password =  models.CharField(max_length=255)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,related_name='designation')
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department')
    zone  = models.ForeignKey(Zonal,on_delete=models.CASCADE,related_name='zone')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
