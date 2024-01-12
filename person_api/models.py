from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)