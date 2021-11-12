from django.db import models

# Create your models here.
class Productos(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.IntegerField()
    paused = models.BooleanField()
    images = models.CharField(max_length=200)
    