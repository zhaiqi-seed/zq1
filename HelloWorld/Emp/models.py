from django.db import models

# Create your models here.
class Emp(models.Model):
    id = models.AutoField(primary_key=True)
    #id = models.IntegerField(primary_key=True)
    empName = models.CharField(max_length=45)
    teacherid = models.ForeignKey("TestModel.Teacher", on_delete=models.CASCADE)
