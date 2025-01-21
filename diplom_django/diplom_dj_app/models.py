from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    species = models.CharField(max_length=10)
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.name