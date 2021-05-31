from django.db import models

# Create your models here.
class Result(models.Model):
    name = models.CharField(max_length=100)
    RollNo = models.IntegerField()
    semester = models.CharField(max_length =10)
    SPI = models.FloatField()
    CPI = models.FloatField()

    #id : int
    #name : str
    #RollNo : int
    #semester : int
    #SPI : float
   # CPI : float

class Contact(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    phno = models.BigIntegerField()
    query = models.TextField()
