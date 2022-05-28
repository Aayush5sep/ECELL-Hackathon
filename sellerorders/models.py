from django.db import models
from django.contrib.auth.models import User
from products.models import ProductList, Products
from user.models import SellerDetails
import datetime
from dateutil.tz import gettz

# Create your models here.


class SeOrders(models.Model):
    order_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(ProductList,on_delete=models.DO_NOTHING)
    purchaser=models.ForeignKey(SellerDetails,on_delete=models.CASCADE)
    current = datetime.datetime.now(tz=gettz('Asia/Kolkata'))
    month=models.IntegerField(default=int(current.month))
    year=models.IntegerField(default=int(current.year))