from django.db import models

# Create your models here.

class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Designation(BaseEntity):
    designation_name = models.CharField(max_length=100,unique=True)
    isauthorised = models.CharField(max_length=10)
    objects = models.Manager()

    def __str__(self):
        return self.designation_name

class Department(BaseEntity):
    department_name = models.CharField(max_length=100,unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.department_name

class Zonal(BaseEntity):
    zonal_name = models.CharField(max_length=150,unique=True)
    objects = models.Manager()

    def __str__(self):
        return  self.zonal_name


class Employee(BaseEntity):
    username = models.CharField(max_length=150,unique=True)
    name = models.CharField(max_length=150)
    password =  models.CharField(max_length=255)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,related_name='designation')
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department')
    zone  = models.ForeignKey(Zonal,on_delete=models.CASCADE,related_name='zone')

    objects = models.Manager()
