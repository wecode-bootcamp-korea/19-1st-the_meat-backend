import bcrypt
import jwt
import json
import mysettings

from django.http import JsonResponse
from .models import User

def LoginDecorator(func):
    def wrapper(self, request, *args, **kwargs):
        
        try:
            access_token       = request.headers['Authorization']
            check_access_token = jwt.decode(access_token, 'secret', algorithms='HS256') 
            user = User.objects.get(id=check_access_token['id']) 
            request.user = user

        except jwt.DecodeError:
            return JsonResponse({"error_code" : "INVALID_TOKEN"}, status=401)

        except user.DoesNotExist:
            return JsonResponse({"error_code" : "UNKNOWN_USER"}, status=401)
        
        except Exception as e:
            return JsonResponse({'message': f"error by {e}"}, status = 400)

        return func(self, request, *args, **kwargs)
    return wrapper 

