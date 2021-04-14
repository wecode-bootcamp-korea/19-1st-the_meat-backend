from django.db                 import models
from django.db.models.deletion import CASCADE
from django.db.models.fields   import URLField


class Categories(models.Model):
    name = models.CharField(max_length = 30)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'categories'
        
class SubCategories(models.Model):
    name     = models.CharField(max_length = 30)
    category = models.ForeignKey('Categories', on_delete = CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'sub_categories'
        
class Products(models.Model):
    name           = models.CharField(max_length = 255)
    price          = models.DecimalField(max_digits = 8, decimal_places = 2)
    discount_rate  = models.DecimalField(max_digits = 3, decimal_places = 2, null = True, blank = True)
    discount_price = models.DecimalField(max_digits = 8, decimal_places = 2, null = True, blank = True)
    unit           = models.DecimalField(max_digits = 3, decimal_places = 2)
    best_before    = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    sub_category = models.ForeignKey('SubCategories', on_delete = CASCADE)
    
    class Meta:
        db_table = "products"
        
class ProductsImages(models.Model):
    image_url = models.URLField(max_length = 255)
    sequences = models.IntegerField()
    
    product = models.ForeignKey('Products', on_delete = CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'product_images'
        
class ProductDescriptions(models.Model):
    image_url = models.URLField(max_length = 255)
    sequences = models.IntegerField()
    
    product = models.ForeignKey('Products', on_delete = CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'product_descriptions'
        
class Reviews(models.Model):
    comment = models.CharField(max_length = 500)
    star    = models.IntegerField()
    
    product = models.ForeignKey('Products', on_delete = CASCADE)
    user    = models.ForeignKey('Users', on_delete = CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'reviews'
        
class ReviewImages(models.Model):
    image_url = models.URLField(max_length = 255)
    
    review = models.ForeignKey('Reviews', on_delete = CASCADE)
    
    class Meta:
        db_table = 'review_images'
        
