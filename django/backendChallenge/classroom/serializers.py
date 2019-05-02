from rest_framework import serializers
from .models import Teacher, Student


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'id',
            'first_name',
            'last_name',
        ]
        read_only_fields = ['id']
    
class StudentReadSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'teacher',
        ]
        read_only_fields = ['id']

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'teacher',
        ]
        read_only_fields = ['id']
