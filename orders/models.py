from django.db import models
from django.db.models.deletion import CASCADE

class Order(models.Model):
    status = models.ForeignKey('OrderStatus', on_delete = CASCADE)
    user   = models.ForeignKey('users.Users', on_delete = CASCADE)
    
    product = models.ManyToManyField('products.Products', through ='ProductsOrder')
    
    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    status = models.SmallIntegerField()
    
    class Meta:
        db_table = 'status'
        
class ProductsOrder(models.Model):
    order   = models.ForeignKey('Order', on_delete = CASCADE)
    product = models.ForeignKey('products.Products', on_delete = CASCADE)
    
    class Meta:
        db_table = 'products_order'