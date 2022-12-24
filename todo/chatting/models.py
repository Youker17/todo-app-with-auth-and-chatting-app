from django.db import models
from django.contrib.auth.models import User
import django

# Create your models here.



class Conversation(models.Model):
    part1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="part1")
    part2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="part2")



class Message(models.Model):
    content = models.TextField()
    date = models.DateField(default=django.utils.timezone.now)
    conv = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


