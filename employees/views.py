from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from employees.models import Department,Designation,Zonal,Employee
from employees.serializer import (EmployeeSerializerPost,EmployeeSerializerGet,DepartmentSerializer,
	DesignationSerializer,ZonalSerializer)


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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeSerializerPost
        return EmployeeSerializerGet

    def get_queryset(self):
    	return Employee.objects.all()