from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Item(models.Model):
    class Priority(models.TextChoices):
        vl="1", "Very Low"
        l="2", "Low"
        m="3", "Medium"
        h="4", "High"
        vh="5", "Very High"
    name=models.CharField(max_length=100)
    early_start_time=models.DateTimeField()
    late_start_time=models.DateTimeField()
    duration=models.IntegerField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    priority=models.CharField(max_length=1, choices=Priority.choices, default=Priority.vl)
    assigned=models.BooleanField(default=False)

