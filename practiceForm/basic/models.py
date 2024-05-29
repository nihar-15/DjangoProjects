from django.db import models

class registration(models.Model):
       first_name=models.CharField(max_length=100)
       last_name=models.CharField(max_length=100)
       email=models.EmailField( max_length=254)
       isAdult=models.BooleanField()
       gender=models.CharField(max_length=15)