from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer, StudentReadSerializer

# Teacher
class TeacherAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TeacherRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all()

# Student
class StudentAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = StudentReadSerializer

    def get_queryset(self):
        return Student.objects.all()

    def post(self, request, *args, **kwargs):
        self.serializer_class = StudentSerializer
        return self.create(request, *args, **kwargs)

class StudentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()
