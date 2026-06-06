from django.db import models

# Create your models here.
from django.db import models

class Account(models.Model):
    pin = models.IntegerField()
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"Account {self.id}"
