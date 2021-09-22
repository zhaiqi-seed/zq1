from django.db import models

# Create your models here.
class DemoList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    url = models.CharField(max_length=400)
    pid = models.IntegerField(default=0)
    level = models.IntegerField(default=0)