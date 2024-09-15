from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    status = models.BooleanField(default=True)
    task_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='team_members') 
