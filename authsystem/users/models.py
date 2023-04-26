from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50),
    address = models.CharField(max_length=250),
    city = models.CharField(max_length=50),
    state = models.CharField(max_length=50),
    zip = models.CharField(max_length=50),
    email = models.EmailField(max_length=50),
    password = models.CharField(max_length=50),
    confirm_password = models.CharField(max_length=50)

def __str__(self):
    return self.first_name