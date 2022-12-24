from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    # status = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)




