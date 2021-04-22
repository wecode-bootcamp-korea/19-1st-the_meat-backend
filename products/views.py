import json

from django.http.response   import JsonResponse
from django.views           import View
from django.core.exceptions import ObjectDoesNotExist

from .models import Product
class ProductView(View):
    pass

class ProductDetailView(View):
    def get(self, request, id):
        try:
            
            product = Product.objects.get(id = id)
            
            result = {
                'id'        : product.id,
                'name'      : product.name,
                'image_url' : [image.image_url for image in product.productimage_set.all()],
                'unit'      : product.unit,
                'real_price': product.get_real_price()['real_price'],
            }
            
            return JsonResponse({'result': result}, status = 200)
        
        except Product.DoesNotExist:
            return JsonResponse({'Error': "Invalid Product"}, status = 400)
        
