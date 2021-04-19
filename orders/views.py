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
    
