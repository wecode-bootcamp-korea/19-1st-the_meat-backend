from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

class Users(models.Model):
    username     = models.CharField(max_length = 20)
    password     = models.CharField(max_length = 255)
    name         = models.CharField(max_length = 16)
    phone_number = models.CharField(max_length = 30)
    email        = models.EmailField(max_length = 60)
    address      = models.CharField(max_length = 100)
   
    user_rank = models.ForeignKey('UserRanks', on_delete = SET_NULL)
    
    class Meta:
        db_table = 'users'
        
class address(models.Model):
    address = models.CharField(max_length = 100)
    
    user = models.ForeignKey('Users', on_delete = CASCADE)
    
    class Meta:
        db_table = 'address'
        
class UserRanks(models.Model):
    rank_name        = models.CharField(max_length = 15)
    previous_payment = models.DecimalField(max_digits = 8, decimal_places = 2)
    
    order = models.ForeignKey('Orders', on_delete = CASCADE)
    
    class Meta:
        db_table = 'user_ranks'
        
class Vouchers(models.Model):
    name            = models.CharField(max_length = 20)
    condition       = models.CharField(max_length = 30)
    expiration_date = models.DateTimeField(auto_now_add = False)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    user         = models.ManyToManyField('Users', through = 'UserVouchers')
    voucher_type = models.ForeignKey('VoucherTypes', on_delete = CASCADE)
    
    class Meta:
        db_table = 'vouchers'
        
class UserVouchers(models.Model):
    user    = models.ForeignKey('Users', on_delete = CASCADE)
    voucher = models.ForeignKey('Vouchers', on_delete = CASCADE)
    is_used = models.SmallIntegerField()
    
    class Meta:
        db_table = 'user_voucher'
        

class VoucherTypes(models.Model):
    name = models.CharField(max_length = 20)
    
    class Meta:
        db_table = 'voucher_types'