from  rest_framework import serializers
from employees.models import Department,Designation,Zonal,Employee

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'



class ZonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zonal
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Employee
        fields = '__all__'
