from django.db import models
from shop.models import Product,Category
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_products')
    total_items = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    
