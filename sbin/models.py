from django.db import models

# Create your models here.

class Bin(models.Model):
    bin_ID = models.CharField(max_length=200)
    Last_cleaned = models.DateTimeField('date published')
    Status = models.IntegerField('Available space in bin, 1-10')

class User(models.Model):
    Binn = models.ForeignKey(Bin, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    Idd = models.CharField(max_length=200)
    Ph_no = models.IntegerField(default=0)
    ratings = models.IntegerField(default=0)