import json
import re
import bcrypt
import jwt

from django.http   import JsonResponse
from django.views  import View 
from .models       import User, UserRank, Address 
from orders.models import Order
from .utils        import LoginDecorator

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        PASSWORD_LENGTH = 8

        email             = data['email']
        name              = data['name']
        phone_number      = data['phone_number']
        password          = data['password']
        confirm_password  = data['confirm_password']
        
        p_email        = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        p_password     = re.compile('^[a-zA-Z0-9]*$')
        p_phone_number = re.compile('[0-9]')
        p_name         = re.compile('^[가-힣]*$')
        
        encoded_pw = password.encode('utf-8')
        hashed_pw  = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())
        
        try:
            if not email or not password or not confirm_password or not phone_number or not name:
                return JsonResponse({'message': 'EMPTY_VALUE'}, status=400)
        
            if not password == confirm_password:
                return JsonResponse({'message': 'PASSWORD DOES NOT MATCH'}, status=400)
        
            if not p_password.search(password):
                return JsonResponse({"message" : "PASSWORD_ERROR"}, status = 400)
        
            if len(password) < PASSWORD_LENGTH:
                return JsonResponse({"message" : "TOO SHORT PASSWORD"}, status = 401)
    
            if not p_email.search(email):
                return JsonResponse({"message" : "EMAIL_FORM_ERROR"}, status = 400)

            if not p_phone_number.search(phone_number):
                return JsonResponse({"message" : "PHONENUMBER_FORM_ERROR"}, status = 400)
            
            if not p_name.search(name):
                return JsonResponse({"message" : "USERNAME"}, status = 400)
        
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "SAME ID EXISTS"}, status = 400)
            
            user_rank_data = UserRank.objects.get(id=3)
            
            user = User.objects.create(
                    email             = data['email'],
                    phone_number      = data['phone_number'],
                    password          = hashed_pw.decode('utf-8'),
                    name              = data['name'],
                    user_rank         = user_rank_data
            ) 

            return JsonResponse({"message" : "Success"}, status = 200)
            
        except KeyError:
            return JsonResponse({'message': 'BAD_REQUEST'}, status=400)

        except Exception as e:
            return JsonResponse({'message': f"error by {e}"}, status = 400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        print(data)
        email = data['email']
        password = data['password']

        try:
            if User.objects.filter(email=data['email']).exists():
                user_email = User.objects.get(email=data['email'])
                
                if bcrypt.checkpw(data['password'].encode('utf-8'), user_email.password.encode('utf-8')):
                    access_token = jwt.encode({'id': user_email.id}, 'secret', algorithm='HS256')
                    return JsonResponse({"token": access_token, "message": "SUCCESS"}, status=200)
                else:
                    return JsonResponse({"message": "INVALID_PASSWORD"}, status=401)
            else:   
                return JsonResponse({"message": "INVALID_EMAIL"}, status=401)
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class AddressView(View):
    @LoginDecorator
    def post(self, request): 
        
        data = json.loads(request.body)
        address = data['address']
        user    = request.user
        
        Address.objects.create(
                address = data['address'],
                user = request.user
        )

        return JsonResponse({'message' : 'SUCCESS'}, status=200)
