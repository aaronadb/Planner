from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=100)
    early_start_time=models.DateTimeField()
    late_start_time=models.DateTimeField()
    duration=models.IntegerField()

class User(AbstractUser):
    pass
    #username=models.CharField(max_length=20, primary_key=True)
    #password=models.CharField(max_length=50)
    #item_list=Item()