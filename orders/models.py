from django.db import models
from django.contrib.auth.models import User
from products.models import Products
from user.models import BuyerDetails
import datetime
from dateutil.tz import gettz

# Create your models here.


class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    order_id=models.AutoField(primary_key=True)
    buyer=models.ForeignKey(BuyerDetails,on_delete=models.CASCADE)
    current = datetime.datetime.now(tz=gettz('Asia/Kolkata'))
    month=models.IntegerField(default=int(current.month))
    year=models.IntegerField(default=int(current.year))