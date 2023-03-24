from django.db import models
from django.contrib.auth.models import AbstractUser
from .manage import *
class CustomUser(AbstractUser):
    # username=None
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=12)
    age=models.CharField(max_length=2)
    gender=models.CharField(max_length=10)
    about=models.CharField(max_length=100)
    
    # objects=UserManager()
    
    # REQUIRED_FIELDS=[]

    # USERNAME_FIELD='email'


