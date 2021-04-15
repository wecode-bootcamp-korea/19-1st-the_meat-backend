from django.db                 import models
from django.db.models.deletion import CASCADE, SET, SET_NULL
        
class User(models.Model):
    username     = models.CharField(max_length = 20)
    password     = models.CharField(max_length = 255)
    name         = models.CharField(max_length = 16)
    phone_number = models.CharField(max_length = 30)
    email        = models.EmailField(max_length = 60)
    main_address = models.CharField(max_length = 100)    
    user_rank    = models.ForeignKey('UserRank', on_delete = CASCADE)
<<<<<<< HEAD
    voucher      = models.ManyToManyField('Voucher', through = 'UserVoucher')
=======
>>>>>>> e4a0d7aecc0ce68ec3c0f9943a0a1c013cfff408
    created_at   = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'users'

class Address(models.Model):
    address    = models.CharField(max_length = 100)
    user       = models.ForeignKey(User, on_delete = CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'addresses'
        
class UserRank(models.Model):
    rank_name        = models.CharField(max_length = 15)
    previous_payment = models.DecimalField(max_digits = 8, decimal_places = 2)
    created_at       = models.DateTimeField(auto_now_add = True)
    updated_at       = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'user_ranks'
        
class Voucher(models.Model):
    name            = models.CharField(max_length = 20)
    condition       = models.CharField(max_length = 30)
    expiration_date = models.DateTimeField(auto_now = False)
<<<<<<< HEAD
=======
    user            = models.ManyToManyField(User, through = 'UserVoucher')
>>>>>>> e4a0d7aecc0ce68ec3c0f9943a0a1c013cfff408
    voucher_type    = models.ForeignKey('VoucherType', on_delete = SET_NULL, null = True)
    created_at      = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'vouchers'
        
class VoucherType(models.Model):
    name       = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'voucher_types'
        
class UserVoucher(models.Model):
    user       = models.ForeignKey(User, on_delete = CASCADE)
    voucher    = models.ForeignKey(Voucher, on_delete = SET_NULL, null = True)
    is_used    = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
        
    class Meta:
    
        db_table = 'user_vouchers'