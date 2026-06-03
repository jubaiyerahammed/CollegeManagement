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

    

