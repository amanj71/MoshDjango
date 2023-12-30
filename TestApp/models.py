from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)

class Section(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Street(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

class Apartment(models.Model):
    number = models.CharField(max_length=10)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
