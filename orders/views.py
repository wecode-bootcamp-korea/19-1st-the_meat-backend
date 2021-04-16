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
        if not User.objects.filter(id = user_id).exist():
            unlogin_user = User.objects.create()
            Order.objects.create(user    = unlogin_user,
                                 product = Product.objects.get(id = data['id']),)

    # try:
        
        



        
        
    #     return JsonResponse({'message': 'status'}, status = 200)
    
    # except:
    #     return None

class OrderView(View):
    pass

