from django.db import models

# Create your models here.


class Student(models.Model):
          
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    email=models.EmailField(unique=True,null=False)
    address=models.TextField(null=True,blank=True)
    image =models.ImageField(null=True)
    certificate=models.FileField(null=True)

