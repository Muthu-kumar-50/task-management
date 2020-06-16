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


class EmployeeSerializerPost(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeSerializerGet(serializers.ModelSerializer):
    designation = DesignationSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    zone  = ZonalSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = ['id','username','name','password','designation','department','zone']
