from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Resume(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Age = models.PositiveIntegerField(null=True,blank=True)
    Nationality = models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30,default='Avaliable')
    Address = models.CharField(max_length=30)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Skype = models.EmailField()
    Languages = models.CharField(max_length=30)

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete =models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

