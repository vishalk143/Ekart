from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    CAT=((1,'Mobile'),(2,'Cloths'),(3,'Shoes'))
    name=models.CharField(max_length=50,verbose_name="Product Name")
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    price=models.FloatField(verbose_name="Product price")
    status=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to="image")

    
'''
    def __str__(self):
        return self.name
'''

    
class cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)
    
class order(models.Model):
    order_id=models.IntegerField()
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    qty=models.IntegerField()