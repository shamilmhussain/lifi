from django.db import models
import datetime

# Create your models here.

class Student(models.Model):
    sid = models.CharField(max_length=15,primary_key = True)
    sname = models.CharField(max_length=30)
    scourse = models.CharField(max_length=30)
    ssem = models.IntegerField()
    sphn = models.BigIntegerField()
    sfine=models.FloatField(default=0)

class Book(models.Model):
    bid = models.CharField(max_length=15, primary_key=True)
    bname = models.CharField(max_length=30)
    bcontent = models.CharField(max_length=30)
    bauthor = models.CharField(max_length=30)
    brackno=models.IntegerField()

class Services(models.Model):
    sid=models.ForeignKey(Student, on_delete=models.CASCADE)
    bid=models.ForeignKey(Book, on_delete=models.CASCADE)
    bdate=models.DateField()
    bcdate=models.DateField()
    rdate=models.DateField(null=True,blank=True)
    bfine=models.FloatField(default=0)