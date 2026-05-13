from django.db import models

# Create your models here.
class Student(models.Model):
    student_id= models.IntegerField()
    student_name=models.CharField(max_length=25)
    student_email=models.EmailField(max_length=30)
    batch=models.IntegerField()
    courses=models.CharField(max_length=30)