from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Item(models.Model):
    name=models.CharField(max_length=100)
    early_start_time=models.DateTimeField()
    late_start_time=models.DateTimeField()
    duration=models.IntegerField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)

