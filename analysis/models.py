from django.db import models
from django.contrib.auth.models import User
from products.models import ProductList
import datetime
from dateutil.tz import gettz

# Create your models here.


class OrderData(models.Model):
    product=models.ForeignKey(ProductList,on_delete=models.DO_NOTHING)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    current = datetime.datetime.now(tz=gettz('Asia/Kolkata'))
    month=models.IntegerField(default=current.month)
    year=models.IntegerField(default=current.year)
    quantity=models.IntegerField(default=0)
    # Product Foreign Key Data Contains:
    # product_id=models.AutoField(primary_key=True)
    # product_name=models.CharField(max_length=200)
    # product_details=models.CharField(max_length=1000)
    # image=models.CharField(max_length=1000,default="https://unsplash.com/photos/sxiSod0tyYQ")