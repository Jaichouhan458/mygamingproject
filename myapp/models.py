from django.db import models

# Create your models here.
class Data(models.Model):  
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    message = models.TextField()
    subject = models.CharField(max_length=255)


class User_Info(models.Model):
    fullname = models.CharField(max_length=10)
    username = models.CharField(unique= True, max_length=20)
    email = models.EmailField(unique=True)
    Password = models.CharField(max_length=10)
   