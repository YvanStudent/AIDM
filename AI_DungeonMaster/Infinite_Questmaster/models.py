# Infinite_Questmaster/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

#this will  contains the user's info and the story the user will create
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # Add more fields if needed or if there is something more we need

class User(AbstractUser):
    password = models.CharField(max_length=128)

class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add more fields if needed or if there is something more we need here as well
