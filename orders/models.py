from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
        
class Order(models.Model):
    status     = models.ForeignKey('OrderStatus', on_delete = SET_NULL, null = True)
    user       = models.ForeignKey('users.User', on_delete = CASCADE)
    product    = models.ManyToManyField('products.Product', through ='ProductOrder')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    order_status = models.SmallIntegerField()
    status_name  = models.CharField(max_length = 12)
    created_at   = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'status'
        
class ProductOrder(models.Model):
    order      = models.ForeignKey(Order, on_delete = SET_NULL, null = True)
    product    = models.ForeignKey('products.Product', on_delete = SET_NULL, null = True)
    quantity   = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
        
    class Meta:
        db_table = 'products_order'