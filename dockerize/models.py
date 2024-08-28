from django.db import models


# Create your models here.
class Animal(models.Model):
    kind = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
