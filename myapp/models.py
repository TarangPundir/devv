from django.db import models
from .models import *

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    sub = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name