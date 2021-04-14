from django.db                 import models
from django.db.models.deletion import CASCADE
from django.db.models.fields   import URLField

class Category(models.Model):
    name = models.CharField(max_length = 30)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'categories'
        
class SubCategory(models.Model):
    name     = models.CharField(max_length = 30)
    category = models.ForeignKey(Category, on_delete = CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'sub_categories'
        
class Product(models.Model):
    name           = models.CharField(max_length = 255)
    price          = models.DecimalField(max_digits = 8, decimal_places = 2)
    discount_rate  = models.DecimalField(max_digits = 3, decimal_places = 2, null = True, blank = True)
    discount_price = models.DecimalField(max_digits = 8, decimal_places = 2, null = True, blank = True)
    unit           = models.DecimalField(max_digits = 3, decimal_places = 2)
    best_before    = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    sub_category = models.ForeignKey('SubCategory', on_delete = CASCADE)
    
    class Meta:
        db_table = "products"
        
class ProductImage(models.Model):
    image_url = models.URLField(max_length = 255)
    sequences = models.IntegerField()
    
    product = models.ForeignKey('Product', on_delete = CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'product_images'
        
class ProductDescription(models.Model):
    image_url = models.URLField(max_length = 255)
    sequences = models.IntegerField()
    
    product = models.ForeignKey('Product', on_delete = CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'product_descriptions'
        
class Review(models.Model):
    comment = models.CharField(max_length = 500)
    star    = models.IntegerField()
    
    product = models.ForeignKey('Product', on_delete = CASCADE)
    user    = models.ForeignKey('users.User', on_delete = CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'reviews'
        
class ReviewImage(models.Model):
    image_url = models.URLField(max_length = 255)
    
    review = models.ForeignKey('Review', on_delete = CASCADE)
    
    class Meta:
        db_table = 'review_images'
        
