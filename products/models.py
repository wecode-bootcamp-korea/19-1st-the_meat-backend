import decimal

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
    original_price = models.DecimalField(max_digits = 12, decimal_places = 2)
    discount_rate  = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    unit           = models.DecimalField(max_digits = 6, decimal_places = 2)
    best_before    = models.IntegerField()
    sub_category   = models.ForeignKey('SubCategory', on_delete = SET_NULL, null = True)
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = "products"
        
    def get_real_price(self):
        if self.discount_rate == 0:
            return {'real_price': self.original_price,
                    self.original_price: 0}
        else:
            return {'real_price': self.original_price * decimal.Decimal(str(1 - self.discount_rate/100))}
        
class ProductImage(models.Model):
    image_url  = models.URLField(max_length = 500)
    sequences  = models.IntegerField()
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
        
class MainImage(models.Model):
    image_url = models.URLField(max_length = 500)
    sequences = models.SmallIntegerField()
    
    class Meta:
        db_table = 'main_images'
        