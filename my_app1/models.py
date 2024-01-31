from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)

class Car(models.Model):
    year = models.IntegerField()
    car_name = models.CharField(max_length=30)
