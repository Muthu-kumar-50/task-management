from django.contrib import admin
from employees.models import Department,Designation,Zonal,Employee

# Register your models here.
admin.site.register([Designation,Department,Employee,Zonal])