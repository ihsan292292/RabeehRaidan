from django.db import models
from adminapp.models import *
# Create your models here.

class Cart(models.Model):
  prod_id = models.IntegerField()
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  qty = models.IntegerField()
  branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
  image = models.ImageField(upload_to='cart/')
  def __str__(self):
    return self.name