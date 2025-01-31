from django.db import models

# Create your models here.
class Data(models.Model):  
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    message = models.TextField()
    subject = models.CharField(max_length=255)
