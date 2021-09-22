from django.db import models

# Create your models here.
class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
class Teacher(models.Model):
    #id = models.IntegerField(primary_key=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.IntegerField(default=0)
    password = models.CharField(max_length=45)

