from django.db import models

# Create your models here.
class DemoList(models.Model):
    id = models.AutoField(primary_key=True)
    demoName = models.CharField(max_length=45)
    demoUrl = models.CharField(max_length=400)