from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=200)
    emp = models.ManyToManyField("Emp.Emp")
    teacher = models.ManyToManyField("TestModel.Teacher")