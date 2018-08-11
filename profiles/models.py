from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)