from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BuyerDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    phone=models.CharField(max_length=10,null=True)
    city=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    country=models.CharField(max_length=50,null=True)

class SellerDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    phone=models.CharField(max_length=10,null=True)
    age=models.IntegerField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
