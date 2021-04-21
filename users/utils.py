import bcrypt
import jwt
import json
import mysettings

from django.http import JsonResponse
from .models import User

def LoginDecorator(func):
    def wrapper(self, request, *args, **kwargs):
        print(1)
        try:
            access_token       = request.headers['Authorization']
            print(2)
            check_access_token = jwt.decode(access_token, 'secret', algorithms='HS256') 
            print(3)
            user = User.objects.get(id=check_access_token['id']) # 위에서 패스워드를 확인하고, 지금 여기서는 유저를 확인하는 과정 근데 토큰만 하면 되는 거 아님?
            # algorithm이 아니라 algorithms였음. 근데 인터넷에서 algorithm로 보고 한 거 같은데..
            # (id=check_access_token['id']) 이 부분 잘 모르겠음. 왜 계속 email이라고 생각을 했지? 
            # 로그인에서 받아온 정보가 email인데 왜 id로 해야 되는지 잘 모르겠음...
            request.user = user # 이 부분을 잘 모르겠음. 다시 공부해야함. 
            print(4)
        except jwt.DecodeError:
            return JsonResponse({"error_code" : "INVALID_TOKEN"}, status=401) 
        # 계속 에러가 나는데 401 INVALID_TOKEN 에러가 계속 나는데, 프린트는 2까지 밖에 안 찍힌다. 
        # 그러면 check_access_token 여기가 잘못이 된건데, 뭔지 모르겠다. 
        except user.DoesNotExist:
            return JsonResponse({"error_code" : "UNKNOWN_USER"}, status=401)
        
        except Exception as e:
            return JsonResponse({'message': f"error by {e}"}, status = 400)

        return func(self, request, *args, **kwargs)
    return wrapper 

