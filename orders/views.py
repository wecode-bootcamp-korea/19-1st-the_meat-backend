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
        data = request.loads(request.body)
        # if not User.objects.filter(id = user_id).exist():
            # Order.objects.create(user = unlogin_user)
        try:
            ProductOrder.objects.create(order = Order.objects.get(user_id = user_id),
                                        product = Product.objects.get(id = data['id']),
                                        quantity = data['quantity'])
        
            return JsonResponse({'message': 'status'}, status = 200)
    
        except KeyError as e:
            return JsonResponse({'Invalid KeyError {}'.format(e)}, status = 400)

class OrderView(View):
    pass

