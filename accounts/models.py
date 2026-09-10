from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
    role_choices=(('organizer','Organizer'),('customer','Customer'))
    role=models.CharField(max_length=100,choices=role_choices,default='customer')
    phone=models.IntegerField(null=True)



