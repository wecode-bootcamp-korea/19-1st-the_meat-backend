import json
from django.core import exceptions
from django.http import response

from django.http.response import JsonResponse
from django.views         import View

from users.utils import LoginDecorator
from .models     import Order, Status

class CartView(View):
    @LoginDecorator
    def post(self, request):
        try:
            data                      = json.loads(request.body)
            user_id                   = request.user
            STATUS_IN_CART            = Status.objects.get(id = 1)
            
            user_order, order_created = Order.objects.get_or_create(user_id   = user_id,
                                                                    status_id = STATUS_IN_CART)
            
            if user_order.productorder_set.filter(product_id = data['id']).exists():
                user_cart           = user_order.productorder_set.get(product_id = data['id'])
                user_cart.quantity += int(data['quantity'])
                user_cart.save()
            else:
                user_cart = user_order.productorder_set.create(order      = user_order,
                                                               product_id = data['id'],
                                                               quantity   = data['quantity'])

            return JsonResponse({'message': 'Success'}, status = 201)
    
        except Order.MultipleObjectsReturned:
            return JsonResponse({'Error': "MORE"}, status = 400)
    
    @LoginDecorator
    def get(self, request):
        try:
            user_id                   = request.user
            STATUS_IN_CART            = Status.objects.get(id = 1)
            user_order, order_created = Order.objects.get_or_create(user_id   = user_id,
                                                                    status_id = STATUS_IN_CART)
            
            if not order_created:
                products = user_order.product.all()
                results = [{
                    'id'         : product.id,
                    'name'       : product.name,
                    'quantity'   : product.productorder_set.get(order   = user_order,
                                                                product = product).quantity,
                    'image_url'  : [image.image_url for image in product.productimage_set.all()],
                    'real_price' : int(product.get_real_price()['real_price']),
                    'total_price': int(product.productorder_set.get(order   = user_order,
                                                                    product = product).get_total_price()),
                    } for product in products]
                
                total_sum = sum([order['total_price'] for order in results])
                
            else: results = []
            
            return JsonResponse({'result': results, 'sum': total_sum}, status = 200)
        
        except Order.MultipleObjectsReturned:
            return JsonResponse({'Error': "MORE"}, status = 400)
        
        except Exception as e:
            return JsonResponse({'Error': f"{e}"}, status = 400)
        
    @LoginDecorator
    def patch(self, request):
        try:
            data                      = json.loads(request.body)
            user_id                   = request.user
            STATUS_IN_CART            = Status.objects.get(id = 1)
            user_order, order_created = Order.objects.get_or_create(user_id   = user_id,
                                                                    status_id = STATUS_IN_CART)
            if not order_created:
                user_cart                = user_order.productorder_set.filter(order   = user_order)
                product_in_cart          = user_order.productorder_set.get(product_id = data['id'])
                product_in_cart.quantity = int(data['quantity'])
                product_in_cart.save()
                            
            total_sum = int(sum([product.get_total_price() for product in user_cart]))
                
            return JsonResponse({'message': 'Success', 'sum': total_sum}, status = 200)
        
        except Order.MultipleObjectsReturned:
            return JsonResponse({'message': "MORE"}, status = 400)
            
    @LoginDecorator
    def put(self, request):
        try:
            data                      = json.loads(request.body)
            user_id                   = request.user
            STATUS_IN_CART            = Status.objects.get(id = 1)
            user_order, order_created = Order.objects.get_or_create(user_id = user_id,
                                                                    status_id = STATUS_IN_CART)

            if not order_created:
                user_order.productorder_set.get(product_id = data['id']).delete()

            products_in_cart = user_order.product.all()
            results = [{
                'id'         : product.id,
                'name'       : product.name,
                'image_url'  : [image.image_url for image in product.productimage_set.all()],
                'quantity'   : product.productorder_set.get(order   = user_order,
                                                            product = product).quantity,
                'real_price' : product.get_real_price()['real_price'],
                'total_price': product.productorder_set.get(order   = user_order,
                                                            product = product).get_total_price()}
                for product in products_in_cart]
                
            total_sum = sum([int(result['total_price']) for result in results])
            
            return JsonResponse({'message': results, 'sum': total_sum}, status = 200)
        
        except Order.MultipleObjectsReturned:
            return JsonResponse({'Error': "MORE"}, status = 400)
        
class OrderBuyView(View):
    @LoginDecorator
    def post(self, request):
        try:
            data                      = json.loads(request.body)
            user_id                   = request.user
            STATUS_IN_CART            = Status.objects.get(id = 1)
            STATUS_IN_BUY             = Status.objects.get(id = 2)
            user_order, order_created = Order.objects.get_or_create(user_id = user_id,
                                                                    status_id = STATUS_IN_CART)
            user_order.status_id = STATUS_IN_BUY
            user_order.save()
            
            Order.objects.create(user_id   = user_id,
                                 status_id = STATUS_IN_CART)
            
            if user_order.productorder_set.all().exists():
                results = [{
                    'id'             : cart.product_id,
                    'name'           : cart.product.name,
                    'original_price' : cart.product.get_real_price()['original_price'],
                    'real_price'     : int(cart.product.get_real_price()['real_price']),
                    'quantity'       : cart.quantity,
                } for cart in user_order.productorder_set.all()]
            else:
                results = []
                
            return JsonResponse({'message':'Success', 'result': results}, status = 200)
        
        except Order.MultipleObjectsReturned:
            return JsonResponse({'Error': "MORE"}, status = 400)