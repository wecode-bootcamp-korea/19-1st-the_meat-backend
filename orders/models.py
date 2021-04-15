from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
        
class Order(models.Model):
<<<<<<< HEAD
    status     = models.ForeignKey('Status', on_delete = SET_NULL, null = True, default = 1)
=======
    status     = models.ForeignKey('OrderStatus', on_delete = SET_NULL, null = True)
>>>>>>> e4a0d7aecc0ce68ec3c0f9943a0a1c013cfff408
    user       = models.ForeignKey('users.User', on_delete = CASCADE)
    product    = models.ManyToManyField('products.Product', through ='ProductOrder')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'orders'

<<<<<<< HEAD
class Status(models.Model):
    status      = models.SmallIntegerField()
    status_name = models.CharField(max_length = 12)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
=======
class OrderStatus(models.Model):
    order_status = models.SmallIntegerField()
    status_name  = models.CharField(max_length = 12)
    created_at   = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)
>>>>>>> e4a0d7aecc0ce68ec3c0f9943a0a1c013cfff408

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