from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, related_name='teacher', on_delete=models.CASCADE)
