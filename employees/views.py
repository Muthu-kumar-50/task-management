from django.shortcuts import render
from rest_framework import viewsets
from employees.models import Department,Designation,Zonal,Employee
from employees.serializer import EmployeeSerializer,DepartmentSerializer,DesignationSerializer,ZonalSerializer


# Create your views here.
class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ZonalViewset(viewsets.ModelViewSet):
    queryset=Zonal.objects.all()
    serializer_class = ZonalSerializer

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
