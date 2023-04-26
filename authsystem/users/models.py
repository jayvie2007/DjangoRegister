from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50, default="Juan")
    middle_name = models.CharField(max_length=50, default="Juan")
    last_name = models.CharField(max_length=50, default="Juan")
    address = models.CharField(max_length=250, default="Juan")
    city = models.CharField(max_length=50, default="Juan")
    state = models.CharField(max_length=50, default="Juan")
    zip = models.CharField(max_length=50, default="Juan")
    username = models.CharField(max_length=50, default="Juan")
    email = models.EmailField(max_length=50, default="Juan")
    password = models.CharField(max_length=50, default="Juan")
    confirm_password = models.CharField(max_length=50, default="Juan")

    def __str__(self):
        return self.first_name