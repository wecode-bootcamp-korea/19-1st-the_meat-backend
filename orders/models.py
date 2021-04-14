from django.db import models
from django.db.models.deletion import CASCADE
        
class Order(models.Model):
    status  = models.ForeignKey('OrderStatus', on_delete = CASCADE)
    user    = models.ForeignKey('users.User', on_delete = CASCADE)
    product = models.ManyToManyField('products.Product', through ='ProductOrder')
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    order_status = models.SmallIntegerField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'status'
        
class ProductOrder(models.Model):
    order   = models.ForeignKey(Order, on_delete = CASCADE)
    product = models.ForeignKey('products.Product', on_delete = CASCADE)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
        
    class Meta:
        db_table = 'products_order'