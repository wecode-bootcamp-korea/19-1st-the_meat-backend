import json
from django.http import response

from django.http.response import JsonResponse
from django.views         import View
from django.db.models     import Q

from .models         import Order, Status, ProductOrder
from users.models    import User
from products.models import Product

class CartView(View):
    # @login_decorator
    def post(self, request):
        try:
            data                      = json.loads(request.body)
            user_id                   = request.user
            user_order, order_created = Order.objects.get_or_create(user_id = user_id, status_id = 1)
            
            if user_order.productorder_set.filter(product_id = data['id']).exists():
                user_cart           = user_order.productorder_set.get(product_id = data['id'])
                user_cart.quantity += int(data['quantity'])
                user_cart.save()
            else:
                user_cart = user_order.productorder_set.create(order      = user_order,
                                                               product_id = data['id'],
                                                               quantity   = data['quantity'])
            result        = {
                'id'       : user_cart.product_id,
                'order_id' : user_cart.order_id,
                'quantity' : user_cart.quantity,
            } 
            return JsonResponse({'result': result}, status = 201)
    
        except Order.MultipleObjectsReturned:
            return JsonResponse({'Error': "MORE"}, status = 400)
    
    # @login_decorator
    def get(self, request):
        try:
            user_id = request.user
            
            user_order, order_created = Order.objects.get_or_create(user_id   = user_id,
                                                                    status_id = 1
                                                                    )
            if not order_created:
                products_in_cart = user_order.product.all()
                results = [{
                    'id'         : product.id,
                    'name'       : product.name,
                    'image_url'  : [image.image_url for image in product.productimage_set.all()],
                    'real_price' : product.get_real_price()['real_price'],}
                    for product in products_in_cart]
            else: results = []
            
            return JsonResponse({'result': results}, status = 200)
        
        except Order.MultipleObjectsReturned:
            return JsonResponse({'Error': "MORE"}, status = 400)
        
    # @login_decorator
    def patch(self, request):
        try:
            data                      = json.loads(request.body)
            user_id                   = data['user_id']
            user_order, order_created = Order.objects.get_or_create(user_id   = user_id,
                                                                    status_id = 1)
            if not order_created:
                product_in_cart          = user_order.productorder_set.get(product_id = data['id'])
                product_in_cart.quantity = int(data['quantity'])
                product_in_cart.save()
    
                results   = [{'id'       : data['id'],
                             'quantity' : product_in_cart.quantity}]
            else:
                results = []
            
            return JsonResponse({'result': "results"}, status = 200)
        
        except Order.MultipleObjectsReturned:
            return JsonResponse({'message': "MORE"}, status = 400)
    
    # @login_decorator
    def put(self, request):
        try:
            data = json.loads(request.body)
            user_id = data.get("user_id")
            
            user_order, order_created = Order.objects.get_or_create(user_id   = user_id,
                                                                    status_id = 1)
            user_cart = user_order.productorder_set.get(product_id = data['id']).delete()

            return JsonResponse({'message': results}, status = 200)
        
        except Order.MultipleObjectsReturned:
            return JsonResponse({'Error': "MORE"}, status = 400)