import json
from django.http import response

from django.http.response import JsonResponse
from django.views         import View
from django.db.models     import Q

from .models         import Order, Status, ProductOrder
from users.models    import User
from products.models import Product

# @loginDecorator
class CartView(View):
    def post(self, request):
        try:
            # user_id    = request.user
            user_id    = 1
            data       = json.loads(request.body)
            user_order = Order.objects.filter(Q(user_id = user_id) & Q(status_id = 1)).first()

            if user_order.productorder_set.filter(product_id=data['id']).exists():
                cart_instance = user_order.productorder_set.get(product_id = data['id'])
                cart_instance.quantity += int(data['quantity'])
                cart_instance.save()
            else:
                ProductOrder.objects.create(order = user_order,
                                            product_id = data['id'],
                                            quantity = data['quantity'])
                
            result_object = user_order.productorder_set.get(product_id = data['id'])
            result        = {
                'id'       : result_object.product_id,
                'order_id' : result_object.order_id,
                'quantity' : result_object.quantity,
            } 
            return JsonResponse({'result': result}, status = 201)
    
        except KeyError as e:
            return JsonResponse({'message': "Invalid KeyError by '{e}'"}, status = 400)
    
    def get(self, request):
        try:
            user_id        = request.user
            in_cart_products = ProductOrder.objects.filter(
                order = Order.objects.filter(Q(user_id = user_id) &
                                             Q(status_id = 1)).first())
            
            results = [{
                'id'         : in_cart_product.product.id,
                'name'       : in_cart_product.product.name,
                'image_url'  : [x.image_url for x in in_cart_product.product.productimage_set.all()],
                'real_price' : in_cart_product.product.get_real_price()['real_price'],
                'total_price': in_cart_product.get_total_price()}
                           for in_cart_product in in_cart_products]

            return JsonResponse({'result': results}, status = 200)
        
        except KeyError as e:
            return JsonResponse({'result': f'Invalid KeyError by {e}'}, status = 400)
        
    def patch(self, request):
        try:
            data = json.loads(request.body)
            user_id        = request.user
            
            in_cart_product = ProductOrder.objects.get(Q(product_id = data['id']) &
                                                       Q(order      = Order.objects.get(Q(user_id = user_id) &
                                                                                      Q(status_id = 1))))
            in_cart_product.quantity = int(data['quantity'])
            in_cart_product.save()
    
            results = {'id'         : data['id'],
                       'quantity'   : in_cart_product.quantity,
                       'total_price': in_cart_product.get_total_price()}
            
            return JsonResponse({'result': results}, status = 200)
        
        except KeyError as e:
            return JsonResponse({'result': f'Invalid KeyError by {e}'}, status = 400)
    
    def put(self, request):
        try:
            user_id = request.user
            data = json.loads(request.body)

            ProductOrder.objects.get(Q(product_id = data['id']) &
                                     Q(order      = Order.objects.get(Q(user_id = user_id) &
                                                                      Q(status_id = 1)))).delete()
            
            return JsonResponse({'message': 'Success'}, status = 200)
        
        except KeyError as e:
            return JsonResponse({'message': f'Invalid KeyError by {e}'}, status = 400)

class OrderView(View):
    def post(self, request):
        pass