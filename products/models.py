from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductList(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=200)
    product_details=models.CharField(max_length=1000)
    image=models.CharField(max_length=1000,default="https://unsplash.com/photos/sxiSod0tyYQ")

class Products(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductList,on_delete=models.CASCADE)
    price=models.CharField(max_length=10,default=0)
    city=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    country=models.CharField(max_length=50,null=True)
