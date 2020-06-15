from  rest_framework import serializers
from employees.models import Department,Designation,Zonal,Employee

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['id','designation_name','isauthorised']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','department_name']



class ZonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zonal
        fields = ['id','zonal_name']


class EmployeeSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer()
    department = DepartmentSerializer()
    zone     = ZonalSerializer()
    

    class Meta:
        model = Employee
        fields = ['id','username','name','password','designation','department','zone']
