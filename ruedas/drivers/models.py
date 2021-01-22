from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    dni = models.IntegerField()
    habilitado = models.BooleanField()
    birth_date = models.DateField()
    signup_date = models.DateField()


def __str___(self):
    return self.first_name


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    kms = models.IntegerField()
