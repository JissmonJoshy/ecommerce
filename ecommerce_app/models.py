from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    Category_name=models.CharField(max_length=100,null=True)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    prname=models.CharField(max_length=255)
    prprice=models.IntegerField(null=True)
    prdesc=models.CharField(max_length=500)
    primg=models.ImageField(upload_to="image/",null=True)

class userdetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200)
    number=models.CharField(max_length=20,null=True)
    usimg=models.ImageField(upload_to="image/",null=True)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    prod=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=1)
    def total_price(self):
        return self.quantity*self.prod.prprice
