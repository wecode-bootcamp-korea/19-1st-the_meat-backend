import json

from django.http.response import JsonResponse
from django.views         import View

from .models         import Order, Status, ProductOrder
from users.models    import User
from products.models import Product

# # @loginDecorator
class AddCartView(View):
    def post(self, request):

        user_id = request.user
        data    = json.loads(request.body)

        try:
            user_product = Product.objects.get(id = data['id'])
            user_orders  = Order.objects.filter(user_id = user_id)
            order        = [user_order for user_order in user_orders if user_order.status.status == 1][0]
            
            if order.product.filter(id=data['id']).exists():
                product_order           = ProductOrder.objects.get(product = user_product)
                product_order.quantity += data['quantity']
                product_order.save()
            else:
                ProductOrder.objects.create(order = order,
                                            product = user_product,
                                            quantity = data['quantity'])

            return JsonResponse({'message': 'Success'}, status = 201)
    
        except KeyError as e:
            return JsonResponse({'message': "Invalid KeyError by \'{}\'".format(e)}, status = 400)
    
    def put(self, request):
        data = json.loads(request.body)
        user_product = Product.objects.get(id = data['id'])
        quantity     = data['quantity']
        total_price  = user_product.get_real_price['real_price'] * quantity
        
        results = {'id': user_product,
                    'quantity': quantity,
                    'total_price': total_price}
        
        return JsonResponse({'result': results}, status = 200)
    
    def delete(self, request):
        data = json.loads(request.body)
        
        ProductOrder.objects.get(product_id = data['id']).delete()
        
        return JsonResponse({'message': 'Success'}, status = 200)
    
class OrderView(View):
    def post(self, request):
        
        
        pass
