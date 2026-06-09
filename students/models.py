from django.db import models
from courses.models import Department, Semester
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    batch = models.CharField(max_length=20)
    courses = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.student_name} ({self.student_id})"

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    roll = models.CharField(max_length=20, unique=True)
    registration_no = models.CharField(max_length=30, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.roll} - {self.first_name} {self.last_name}"