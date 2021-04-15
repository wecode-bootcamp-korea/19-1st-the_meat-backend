from django.db                 import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields   import URLField

class Category(models.Model):
    name       = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'categories'
        
class SubCategory(models.Model):
    name       = models.CharField(max_length = 30)
    category   = models.ForeignKey(Category, on_delete = CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'sub_categories'
        
class Product(models.Model):
    name           = models.CharField(max_length = 100)
<<<<<<< HEAD
    price          = models.DecimalField(max_digits = 10, decimal_places = 2)
    discount_rate  = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    real_price     = models.DecimalField(max_digits = 10, decimal_places = 2)
    unit           = models.DecimalField(max_digits = 5, decimal_places = 2)
=======
    price          = models.DecimalField(max_digits = 8, decimal_places = 2)
    discount_rate  = models.DecimalField(max_digits = 3, decimal_places = 2, default = 0)
    discount_price = models.DecimalField(max_digits = 8, decimal_places = 2, default = price)
    unit           = models.DecimalField(max_digits = 3, decimal_places = 2)
>>>>>>> e4a0d7aecc0ce68ec3c0f9943a0a1c013cfff408
    best_before    = models.IntegerField()
    sub_category   = models.ForeignKey('SubCategory', on_delete = SET_NULL, null = True)
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = "products"
        
class ProductImage(models.Model):
    image_url  = models.URLField(max_length = 500)
    sequence   = models.IntegerField()
    product    = models.ForeignKey('Product', on_delete = CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'product_images'
        
class ProductDescription(models.Model):
    image_url  = models.URLField(max_length = 500)
    sequences  = models.IntegerField()
    product    = models.ForeignKey('Product', on_delete = CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'product_descriptions'
        
class Review(models.Model):
    comment    = models.CharField(max_length = 500)
    rating     = models.IntegerField()
    product    = models.ForeignKey('Product', on_delete = CASCADE)
    user       = models.ForeignKey('users.User', on_delete = CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'reviews'
        
class ReviewImage(models.Model):
    image_url = models.URLField(max_length = 500)
    review    = models.ForeignKey('Review', on_delete = CASCADE)
    
    class Meta:
        db_table = 'review_images'