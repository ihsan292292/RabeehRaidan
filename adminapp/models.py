from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.


    
class Branch(models.Model):
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    gmap = models.URLField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.location
    

class Staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50,null=True,blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username 
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')
    def __str__(self):
        return self.name
    
class Order(models.Model):
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField()
    location = models.ForeignKey(Branch,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.user.username
    
