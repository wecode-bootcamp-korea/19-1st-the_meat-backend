import json
<<<<<<< HEAD
from theMeat.users.models import User

from django.http.response import JsonResponse
from django.views         import View

from .models         import Order, Status, ProductOrder
from products.models import Product

# @loginDecorator
class AddCartView(View):
    def post(self, request):
        
        # user = request.user
        try:
            data = json.loads(request.body)
            
            # if not Order.objects.filter(user_id = request.user).exist:
            #     Order.objects.create(status=Status.objects.get(id=2),
            #                          user = User.objects.get(id=request.user)
            #                          )
            # if Order.objects.get(user_id = request.user).status_id != 3:
            #     None

            
            
            return JsonResponse({'message': 'status'}, status = 200)
        
        except:
            return None
=======

from django.views import View

# from .models import *

class OrderView(View):
    pass
>>>>>>> e4a0d7aecc0ce68ec3c0f9943a0a1c013cfff408
