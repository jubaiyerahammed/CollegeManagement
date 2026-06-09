from django.db import models

# Create your models here.
from django.db import models

class StudentsInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    batch = models.IntegerField()
    password = models.CharField(max_length=128)
    re_password = models.CharField(max_length=128)   # hashed password store করার জন্য
    textarea = models.TextField()
    payments= models.DecimalField(max_digits=6, decimal_places=2)

    
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    credit = models.IntegerField(default=3)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Semester(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
