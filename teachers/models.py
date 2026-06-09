from django.db import models

# Create your models here.
from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True, null=True)
    join_date = models.DateField()
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="teachers/photos/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
